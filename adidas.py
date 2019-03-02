# Import libraries
import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pyvirtualdisplay import Display


driver = webdriver.Firefox()
# Set the URL you want to webscrape from
url="https://www.adidas.com/us/men-basketball-shoes"
# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup object
soup = BeautifulSoup(response.text, "html.parser")

# To download the whole data set, let's do a for loop through all a tags
i=0
while i<len(soup.find_all('div','gl-product-card')):
    print(soup.find_all('div','gl-product-card__name')[i].string)
    print(soup.find_all('span','gl-price__value')[i].string)
    i+=1







#https://www.adidas.com/us/men-basketball-shoes