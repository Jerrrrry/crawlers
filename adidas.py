# Import libraries

#!/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url="https://www.gasbuddy.com/GasPrices/California/Riverside"
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.setExperimentalOption('useAutomationExtension', false)
#options.setBinary("/var/chromedriver/chromedriver")
chromeDriverPath = "/var/chromedriver/chromedriver"
driver = webdriver.Chrome(chromeDriverPath,chrome_options=options)
print('initiating chrome driver')

print('start display')
sleep(4)

driver.get(url)

try:
    element=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@class='gb-price']")))
finally:
    #divs=driver.find_elements_by_xpath("//div[@data-analytics-link='article']")
    #print(len(divs))
    prices=driver.find_elements_by_class_name("gb-price")
    lines=driver.find_elements_by_class_name("accordion-toggle")
    for i in range(len(lines)):
        print(prices[i].text)
        print(lines[i])
    driver.quit()

print('get url')




#elements = driver.find_elements_by_class_name("mn-person-card__person-btn-ext.button-secondary-medium")


#find_elements_by_class_name


#https://www.adidas.com/us/men-basketball-shoes
#'.//*[@class="price ng-scope ng-binding"]'

#mine

#"//div[@class='gl-price']"

#driver.find_element_by_xpath("//button[@class='mn-person-card__person-btn-ext button-secondary-medium']").click()
