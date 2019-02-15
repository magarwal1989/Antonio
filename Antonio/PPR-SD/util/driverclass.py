import os
from selenium import webdriver
from selenium.common.exceptions import *
from urllib.error import URLError
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
ChromeDriverExePath = os.path.join(PROJECT_ROOT,'chromedriver.exe')

class driverClass():
    @staticmethod
    def register_driver():
      
        return driverClass.get_web_driver()

    @staticmethod
    def get_web_driver():
        
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-infobars")
        Chrome=webdriver.Chrome(ChromeDriverExePath,chrome_options=chrome_options)
        Chrome.implicitly_wait(2)
        return Chrome
