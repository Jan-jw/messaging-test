from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.login_page import LoginPage
from utilities.cookies_handler import CookiesHandler
from utilities.read_properties import ReadConfig
import time


class TestLogin:
    # class variable
    baseURL = ReadConfig.get_applicationURL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_login(self):
        self.browser = webdriver.Chrome()
        self.browser.get(self.baseURL)
        login_page = LoginPage(self.browser)
        login_page.signin_page()  # load the login in page
        self.browser.implicitly_wait(10)  # implicit wait for sign in page to load

        # account for possible image-based captcha - semi automation
        time.sleep(10)

        # https://www.ebay.com/signin/
        # title= Sign in or Register | eBay
        login_page.set_username(self.username)
        login_page.click_cont()

        try:
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, login_page.password_txt_id))
            )
            login_page.set_password(self.password)
            login_page.click_signin()

            # possible otp

            # save cookies
            CookiesHandler.read_cookies(self.browser.get_cookies())
        except:
            print("login fail: cannot locate password")

        self.browser.close()
