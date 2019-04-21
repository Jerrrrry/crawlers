# Import libraries
import requests
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url="https://www.99ranch.com/weekly-special"
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
i=0
while i<len(soup.find_all('div','stores-weekly')):
    print(soup.find_all('div','stores-weekly')[i].h3.string)
    print(soup.find_all('div','stores-weekly')[i].children[3])
    for child in soup.find_all('div','stores-weekly')[i].children:
        print(child)
    #content=BeautifulSoup(soup.find_all('div','stores-weekly'),"html.parser")

    #if content.find_all('weekly-store-special'):
        #print(content.find_all('weekly-store-special')[0])
    i+=1