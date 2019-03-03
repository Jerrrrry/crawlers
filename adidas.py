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
chromeDriverPath = "/var/chromedriver/chromedriver"
driver = webdriver.Chrome(chrome_options=options)
print('initiating chrome driver')
#display = Display(visible=0, size=(800, 600))
#display.start()

print('start display')


sleep(4)

driver.get(url)
sleep(randint(2,3))

for div in driver.find_elements_by_xpath('//div[@class="gl-product-card__name gl-label gl-label--medium"]//'):
	print(div)

#display.stop()
driver.quit()





#https://www.adidas.com/us/men-basketball-shoes