#!/usr/bin/env python
import datetime
import json
import os, platform
import re
import requests
import sys
import time
try:
  from BeautifulSoup import BeautifulSoup
except ImportError:
  from bs4 import BeautifulSoup

# Create JSON function
def finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, component_port, css_color, tested_url):
    json_values = {
	'environment_name': '%s' %environment_name,
	'component_name': '%s' %component_name,
    'host_name': '%s' %host_name,
	'ip_address': '%s' %ip_address,
	'sl_private_ip_address': '%s' %sl_private_ip_address,
	'comments': '%s' %comments,
    'ports': '%s' %ports,
    'status_code': '%s' %status_code,
    'request_message': '%s' %request_message,
    'component_port': '%s' %component_port,
    'css_color': '%s' %css_color,
    'tested_url': '%s' %tested_url,
    }
    print json_values
    json_value_comma = json_values
    write_to_json_file(json_value_comma)

#Creates directories if they don't exist
def make_dirs(input_dir):
    folder = os.path.dirname(input_dir)
    if not os.path.exists(folder):
        os.makedirs(folder)

#input_json is JSON to be written, input_filename is the filename specified
#input_filename can be submitted as "/service/ansible/monitor_name/monitor_name.json", directories will be created
def write_to_json_file(input_json):
    split_dir, split_file = os.path.split(datetime_filename)
    final_filename = split_file
    if split_dir:
        final_filename = split_dir + "/" + split_file
        make_dirs(split_dir + "/")
        if not os.path.exists(split_dir):
            time.sleep(2)
    target_output_file = open(final_filename, "a")
    target_output_file.write(json.dumps(input_json, sort_keys=True, indent=4, separators=(',',': ')))
    target_output_file.write(',\n')
    target_output_file.close()

# Create variable for unix time, set the desired filename
unix_time = str(int(time.time()))
datetime_filename = './aemparseresults/' + unix_time  + 'aem_check.json'

# Get APIC Confluence page
r = requests.get('https://opteam.lvdc.kp.org/mw/index.php/AEM_Environments', verify=False)

# FOR TESTING LOCALLY
#r = open("file","rb")
#html = r.read()
#parsed_html = BeautifulSoup(html, 'lxml')
#pretty_html = parsed_html.prettify()

html = r.content
soup = BeautifulSoup(html, 'lxml')

all_rows = soup.select('table > tr')
amount_of_rows = len(all_rows)
print amount_of_rows
# How many times to iterate based on number of tr tags found

global previous_env
global css_color
previous_env = ""
css_color = ""

i = 0
while i < amount_of_rows:
  current_row = all_rows[i]
#  print current_row

  # Add 1 to iterator
  i += 1

  if current_row.find('td'):
    # Find Environment Headers
    #print current_row.text.strip().split('\n')
    split_row = current_row.text.strip().split('\n')
    if "Prod" in split_row[0].strip() or "Preview" in split_row[0].strip():
      continue

    environment_name = split_row[0].strip()

    if previous_env is "" and css_color is "":
      previous_env = environment_name
      css_color = "0"
    elif previous_env is environment_name:
      previous_env = environment_name
      css_color = css_color
    elif previous_env != environment_name:
      previous_env = environment_name
      if css_color is "0":
        css_color = "1"
      elif css_color is "1":
        css_color = "0"

    component_name = split_row[1].strip()
    host_name = split_row[2].strip()
    ip_address = split_row[3].strip()
    try:
      if split_row[6]:
        ports = split_row[6].strip()
    except IndexError:
      ports = 'N/A'
      pass
    try:
      if split_row[5]:
        comments = split_row[5].strip()
    except IndexError:
      comments = 'N/A'
      pass
    try:
      if split_row[4]:
        sl_private_ip_address = split_row[4].strip()
    except IndexError:
      sl_private_ip_address = 'N/A'
      pass
    print environment_name.lower()
    if "Disp" in component_name:
      component_port = "44301"
    elif "Auth" in component_name:
      component_port = "4502"
    elif "Pub" in component_name:
      component_port = "4503"
    else:
      component_port = "None Found"

    if "Pub" in component_name and "Disp" not in component_name:
      try:
        constructed_url = "http://" + host_name + ":" + component_port + '/content/kporg/en/national.html'
        r = requests.get("http://" + host_name + ":" + component_port + '/content/kporg/en/national.html', timeout=15, verify=False, allow_redirects=True)
        print r.status_code
        status_code = r.status_code
        request_message = r.raise_for_status()
        finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, component_port, css_color, constructed_url)
      except requests.exceptions.RequestException as e:
        try:
          constructed_url = "https://" + host_name + ":" + "5433" + '/content/kporg/en/national.html'
          r = requests.get("https://" + host_name + ":" + "5433" + '/content/kporg/en/national.html', timeout=15, verify=False, allow_redirects=True)
          print r.status_code
          status_code = r.status_code
          request_message = r.raise_for_status()
          finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, "5433", css_color, constructed_url)
        except requests.exceptions.RequestException as e:
          constructed_url = "https://" + host_name + ":" + "5433" + '/content/kporg/en/national.html'
          status_code = r.status_code
          request_message = "4503 & 5433 Failed; " + str(e)
          finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, "4503, 5433", css_color, constructed_url)
    else:
      try:
        constructed_url = "http://" + host_name + ":" + component_port
        r = requests.get("http://" + host_name + ":" + component_port, timeout=15, verify=False, allow_redirects=True)
        print r.status_code
        status_code = r.status_code
        request_message = r.raise_for_status()
        finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, component_port, css_color, constructed_url)
      except requests.exceptions.RequestException as e:
        try:
          constructed_url = "https://" + host_name + ":" + component_port
          r = requests.get("https://" + host_name + ":" + component_port, timeout=15, verify=False, allow_redirects=True)
          print r.status_code
          status_code = r.status_code
          request_message = r.raise_for_status()
          finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, component_port, css_color, constructed_url)
        except requests.exceptions.RequestException as e:
          constructed_url = "https://" + host_name + ":" + component_port
          status_code = r.status_code
          request_message = "http & https Failed; " + str(e)
          finalize_json(environment_name, component_name, host_name, ip_address, sl_private_ip_address, comments, ports, status_code, request_message, component_port, css_color, constructed_url)

# Clean up file, add brackets to final JSON
with open(datetime_filename, 'r') as original_file:
  original_data = original_file.read()
  cleaned_original_data = re.sub('.{1}$', '', original_data)
with open(datetime_filename, 'w') as finalized_file:
  finalized_file.write("[\n" + cleaned_original_data + "]")