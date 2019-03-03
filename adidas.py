# Import libraries

#!/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = "https://store.nike.com/us/en_us/pw/mens-basketball-shoes/7puZ8r1Zoi3?ipp=62"
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chromeDriverPath = "/var/chromedriver/chromedriver"
driver = webdriver.Chrome(chromeDriverPath,chrome_options=options)
print('initiating chrome driver')

print('start display')


sleep(4)

driver.get(url)

print('get url')
sleep(4)
divs=driver.find_elements_by_xpath("//div[@class='grid-item-content']")
for div in divs:
    print(1)
driver.quit()





#https://www.adidas.com/us/men-basketball-shoes
#'.//*[@class="price ng-scope ng-binding"]'

#mine

#"//div[@class='gl-price']"