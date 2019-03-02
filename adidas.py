# Import libraries

#!/bin/python
# -*- coding: utf-8 -*-

from time import sleep
from random import randint
from selenium import webdriver
from pyvirtualdisplay import Display

driver = webdriver.Chrome("/var/chromedriver/chromedriver")
url = "https://www.adidas.com/us/men-basketball-shoes"

display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome("/var/chromedriver/chromedriver")
sleep(4)

driver.get(url)
sleep(randint(2,3))

for div in driver.find_elements_by_xpath('//div[@class="gl-product-card__name gl-label gl-label--medium"]//'):
	print(div)





#https://www.adidas.com/us/men-basketball-shoes