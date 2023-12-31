from time import time
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from utlility import Utility

start = time()  # Starting time
print("Initiating the process....")

##### Selenium Chrome Driver
options = Options()
driver = webdriver.Chrome() #Chrome window opens up
login_page_url = "https://twitter.com/i/flow/login?lang=en"
userhandle_page_urls = [
    #"https://twitter.com/the_hindu" ,
    #                      "https://twitter.com/timesofindia",
                         #  "https://twitter.com/Telegraph",
                         # "https://twitter.com/thewire_in",
                         # "https://twitter.com/IndianExpress",
                         "https://twitter.com/HindustanTimes"


                         ]
driver.maximize_window() # Maximises the winoow
driver.get(login_page_url) # This will enter the starting url in search bar and laod it
utility = Utility()  # Repository for all the functions
print("Selenium version:", selenium.__version__)
utility.sign_in(driver=driver)
# WE reach to homepage at this point. Now we search for our first Userhandle to scrape tweets from.
# utility.search_feature(driver=driver)

for index,user in enumerate(userhandle_page_urls):
    utility.open_user_handle(link=userhandle_page_urls[index], driver=driver, login_flag= True if index==0 else False)

while True:
    pass
