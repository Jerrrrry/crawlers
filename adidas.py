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
driver.implicitly_wait(10)
driver.get(url)

print('get url')
sleep(2)
divs=driver.find_elements_by_xpath("//div[@class='gl-product-card__name gl-label gl-label--medium']")

print(len(divs))
#divs=driver.find_elements_by_class_name("gl-product-card__name")
for div in divs:
    print(1)
driver.quit()


#elements = driver.find_elements_by_class_name("mn-person-card__person-btn-ext.button-secondary-medium")


#find_elements_by_class_name


#https://www.adidas.com/us/men-basketball-shoes
#'.//*[@class="price ng-scope ng-binding"]'

#mine

#"//div[@class='gl-price']"

#driver.find_element_by_xpath("//button[@class='mn-person-card__person-btn-ext button-secondary-medium']").click()
