# Import libraries
import requests
import time
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url="https://store.nike.com/us/en_us/pw/mens-basketball-shoes/7puZ8r1Zoi3?ipp=62"
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
i=0
while i<len(soup.find_all('div','grid-item-content')):
    print(soup.find_all('p','product-display-name')[i].string)
    print(soup.find_all('span','local nsg-font-family--base')[i].string)
    i+=1