from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login_page import LoginPage
from utilities.cookies_handler import CookiesHandler
from utilities.read_properties import ReadConfig
import time
from pageObjects.home_page import HomePage
from selenium.webdriver.common.action_chains import ActionChains



class TestMessage:
    baseURL = ReadConfig.get_applicationURL()
    loginURL = ReadConfig.get_loginURL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_msg_page_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh() #refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()
        time.sleep(3)
        title = self.driver.title

        if title == "My eBay: Messages":
            self.driver.close()
            assert True
        else:
            # ebay may redirect to login again
            self.driver.close()
            assert False

    # def test_msg_page_title(self):
#          ,
