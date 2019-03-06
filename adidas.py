# Import libraries

#!/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

url="https://www.adidas.com/us/men-basketball-shoes"
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

try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@data-auto-id='plp-header-bar-products-count']")))
finally:
    divs=driver.find_elements_by_xpath("//h2[@class='product-name']")
    print(len(divs))
    #divs=driver.find_elements_by_class_name("gl-product-card__name")
    for div in divs:
        print(1)
    driver.quit()

print('get url')




#elements = driver.find_elements_by_class_name("mn-person-card__person-btn-ext.button-secondary-medium")


#find_elements_by_class_name


#https://www.adidas.com/us/men-basketball-shoes
#'.//*[@class="price ng-scope ng-binding"]'

#mine

#"//div[@class='gl-price']"

#driver.find_element_by_xpath("//button[@class='mn-person-card__person-btn-ext button-secondary-medium']").click()
