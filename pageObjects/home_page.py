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


# from selenium import webdriver
class HomePage:
    signin_page_linktxt = "Sign in"
    user_drpdown_xpath = "//li[@id='gh-eb-My']"
    sub_menu_xpath = "//div[@id='gh-eb-My-o']"
    msg_menuitem_xpath = "//body[1]/header[1]/div[1]/ul[2]/li[3]/div[1]/div[1]/ul[1]/li[11]"

    def __init__(self, driver):
        self.driver = driver

    def signin_page(self):
        self.driver.find_element(By.LINK_TEXT, self.signin_page_linktxt).click()

    def user_messages_page(self):
        # CookiesHandler.write_cookies(self.driver)
        # self.driver.refresh()  # refresh after adding cookies
        # self.driver.implicitly_wait(5)  # implicit wait for sign in page to load

        actions = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.user_drpdown_xpath))
        )
        drp_menu = self.driver.find_element(By.XPATH, self.user_drpdown_xpath)
        actions.move_to_element(drp_menu)

        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.LINK_TEXT, home_page.msg_menuitem_linktxt))
        # )
        sub = self.driver.find_element(By.XPATH, self.sub_menu)
        actions.move_to_element(sub)
        msg = self.driver.find_element(By.XPATH, self.li)
        actions.click(msg)
        actions.perform()

