import csv
import json
import argparse
from time import time
from selenium.webdriver.common.by import By

from datetime import datetime
from urllib.parse import urljoin


from selenium.webdriver.support.ui import WebDriverWait

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from utlility import Utility

start = time()  # Starting time
print("Initiating the process....")
##### Selenium Chrome Driver
options = Options()
driver = webdriver.Chrome(

)
driver.maximize_window()
driver.get("https://twitter.com/i/flow/login?lang=en")
utility = Utility()

utility.sign_in(driver=driver)
utility.search_feature(driver=driver)
utility.open_tweeet(link="https://twitter.com/mohakmangal/status/1690720610358296576", driver=driver)
# text=driver.find_element(By.XPATH,value = 'wvjLuicTEJvzCj3').text
# print(text)

# to fetch the text of element


while True:
    pass



