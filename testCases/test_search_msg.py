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
from pageObjects.messages_page import MessagesPage

class TestSearchMsg:
    baseURL = ReadConfig.get_applicationURL()
    loginURL = ReadConfig.get_loginURL()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()
    test_sender = ""
    test_subject = "Re:"
    test_time = "10/12/22"

    # search in all messages
    def test_all_sender(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.search_bar(self.test_sender)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_all_subject(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.search_bar(self.test_subject)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_all_time(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.search_bar(self.test_sender)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    # search in members messages
    def test_member_sender(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("members")
        msg_page.search_bar(self.test_sender)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_member_subject(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("members")
        msg_page.search_bar(self.test_subject)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_member_time(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("members")
        msg_page.search_bar(self.test_time)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    # search in eBay messages
    def test_eBay_sender(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("eBay")
        msg_page.search_bar(self.test_sender)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_eBay_subject(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("eBay")
        msg_page.search_bar(self.test_subject)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True

    def test_eBay_time(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseURL)
        CookiesHandler.write_cookies(self.driver)
        self.driver.refresh()  # refresh after adding cookies
        self.driver.implicitly_wait(5)  # implicit wait for sign in page to load
        home_page = HomePage(self.driver)
        home_page.user_messages_page()

        msg_page = MessagesPage(self.driver)
        msg_page.show_tab("eBay")
        msg_page.search_bar(self.test_time)
        # results panel appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, msg_page.result_div_id))
        )
        result = self.driver.find_element(By.ID, msg_page.result_div_id)
        result_msg = result.find_element(By.TAG_NAME, "p").text
        if result_msg == "You do not have any messages that meet your search criteria.":
            self.driver.close()
            assert False
        elif "2 messages" in result_msg:
            self.driver.close()
            assert True