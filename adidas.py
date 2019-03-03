# Import libraries

#!/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options as ChromeOptions

url = "https://www.adidas.com/us/men-basketball-shoes"
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
#divs=driver.find_elements_by_xpath("//div[@class='grid-item-content']")
divs=driver.find_elements_by_class_name("gl-product-card__name gl-label gl-label--medium")
for div in divs:
    print(1)
driver.quit()


#find_elements_by_class_name


#https://www.adidas.com/us/men-basketball-shoes
#'.//*[@class="price ng-scope ng-binding"]'

#mine

#"//div[@class='gl-price']"