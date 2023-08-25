from selenium.webdriver.support.ui import WebDriverWait
import json
from selenium import webdriver
import re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC


class Utility:

    def __init__(self):
        self.timeout = 100
        f = open('constants.json')
        data = json.load(f)
        self.configData = data

        f.close()
        pass

    def sign_in(self, driver):
        # element_present = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
        #                                                                                   self.configData[
        #                                                                                       "user_name_xpath"])))
        # # Wait for a maximum of 10 seconds until the element with the given selector is clickable
        # element_clickable = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
        #                                                                                self.configData['user_name_xpath'])))
        # input_field_visible = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,
        #                                                                                        "user_name_xpath")))
        # Wait for a maximum of 10 seconds until the input field with the given selector is clickable
        input_field_interactable = WebDriverWait(driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                         self.configData[
                                                                                                             "user_name_xpath"])))

        input_field_interactable.send_keys(self.configData['user_name'])  # Enter data into the input field
        ## STEP 2: Click on the next Button:

        next_button_clickable = WebDriverWait(driver, timeout=self.timeout).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                              self.configData[
                                                                                                                  'next_button_xpath'])))
        next_button_clickable.click()
        ## STEP 3: Enter the pasword in password field.
        password_field_interactable = WebDriverWait(driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                            self.configData[
                                                                                                                "password_field_xpath"])))
        password_field_interactable.send_keys(self.configData['password'])

        ## STEP 4: CLick on the login button:

        login_button_interactable = WebDriverWait(driver, timeout=self.timeout).until(
            EC.element_to_be_clickable((By.XPATH,
                                        self.configData['login_button_xpath'])))
        login_button_interactable.click()

    def search_feature(self, driver):
        search_field_interactable = WebDriverWait(driver, self.timeout).until(EC.element_to_be_clickable((By.XPATH,
                                                                                                          self.configData[
                                                                                                              "search_field_xpath"])))

        search_field_interactable.send_keys("NullCon Delhi")
        search_field_interactable.send_keys(Keys.RETURN)  # Enter data into the input field

    def open_tweeet(self, driver: webdriver.Chrome, link):
        print(f"Tweet Link: ${link}")
        driver.get(link)
        # Wait for a maximum of 20 seconds for the document.readyState to be 'complete'
        wait = WebDriverWait(driver, timeout=self.timeout)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        from selenium import webdriver

        # Create a WebDriver instance and navigate to the tweet URL

        # Wait for the tweet text element to be present
        #
        input_field_visible = WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH,

                                                                                                "//div[@data-testid='tweetText']")))
        print(input_field_visible.text)

        find_replies =  driver.find_elements(By.XPATH,value="//div[@data-testid='cellInnerDiv']")

        print(len(find_replies))

        for reply in find_replies:
            for s in re.findall(r'(.*?)(?:\n\n|\n$)', reply.text    , flags=re.S):
                print(re.match(r'(.*?)(?=\d|\n)', s)[0])

        # # Get the text content of the tweet
        # tweet_text = tweet_text_element.text
        # print("Tweet Text:", tweet_text)

        # Close the WebDriver
        driver.quit()
