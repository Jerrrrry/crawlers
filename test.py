# Import libraries
import requests
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url="https://www.gasbuddy.com/GasPrices/California/Riverside"
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
i=0
while i<len(soup.find_all('tr','accordion-toggle')):
    #print(soup.find_all('p','product-display-name')[i].string)
    #print(soup.find_all('span','local nsg-font-family--base')[i].string)
    print(soup.find_all('tr','accordion-toggle')[i].contents[1].contents)
    i+=1