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

class MessagesPage:
    # search messages
    # search text box searches messages within the current folder
    search_txtbox_xpath = "//form[@id='kwdform']//input[@id='keyword']"
    search_btn_id = "searchglass"

    # advance search
    advsearch_drpdown_id = "advsea"
    searchby_sender_name_id = "searchSenderName"
    search_sender_txt_xpath = "//input[@id='searchSenderName']"
    searchby_subject_id = "searchSubject"
    # searchby_itemId_id = "searchItemId"
    # searchby_item_title_id = "searchItemTitle"
    searchby_start_date_id = "searchStartDate"
    searchby_end_date_id = "searchEndDate"
    folder_drpmenu_id = "dropdown_searchFolderId"
    all_msg_menuitem_id = "searchFolderId_0"
    member_msg_menuitem_id = "searchFolderId_1"
    eBay_msg_menuitem_id = "searchFolderId_2"
    sent_msg_menuitem_id = "searchFolderId_4"
    trash_msg_menuitem_id = "searchFolderId_5"
    archive_msg_menuitem_id = "searchFolderId_6"
    folder_msg_menuitem_id = "searchFolderId_7"
    advsearch_btn_id = "search-submit"
    search_close_id = "oly-close"

    # result panel
    result_div_id = "controller-status"


    # filter messages
    all_msg_tab_id = "all_unread_c"
    members_tab_id = "m2m_unread_c"
    eBay_tab_id = "ebay_unread_c"
    sent_msg_linktxt = "Sent"
    trash_tab_linktxt = "Trash"
    archive_tab_linktxt = "Archive"
    # folder_tab_linktxt = ""

    # move messages
    move_to_drpdown_xpath = "//a[@id='w1-8']"
    ul_menu_id = "menu_w1-8"
    trash_item_linktxt = "Trash"
    archive_item_linktxt = "Archive"
    # folder_item_linktxt

    delete_btn_xpath = "//button[contains(text(),'Delete')]"
    archive_btn_xpath = "//button[contains(text(),'Archive')]"

    def __init__(self, driver):
        self.driver = driver

    # def delete_msg(self, location):

    # def archive_msg(self, location):

    def move_to_drpdown(self, location):
        self.driver.find_element(By.XPATH, self.move_to_drpdown_xpath).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, self.ul_menu_id))
        )
        if location == "Trash":
            self.driver.find_element(By.LINK_TEXT, self.trash_item_linktxt).click()
        elif location == "Archive":
            self.driver.find_element(By.LINK_TEXT, self.archive_item_linktxt).click()
        else: # all msg
            self.driver.find_element(By.LINK_TEXT, location).click()

    def show_tab(self, type):
        if type == "all":
            self.driver.find_element(By.ID, self.all_msg_tab_id).click()
        elif type == "members":
            self.driver.find_element(By.ID, self.members_tab_id).click()
        elif type=="eBay":
            self.driver.find_element(By.ID, self.eBay_tab_id).click()
        elif type == "sent":
            self.driver.find_element(By.LINK_TEXT, self.sent_msg_linktxt).click()
        elif type == "trash":
            self.driver.find_element(By.LINK_TEXT, self.trash_tab_linktxt).click()
        elif type == "archive":
            self.driver.find_element(By.LINK_TEXT, self.archive_tab_linktxt).click()
        else: # FOLDER
            self.driver.find_element(By.LINK_TEXT, type).click()

    def search_bar(self, text):
        self.driver.find_element(By.XPATH, self.search_txtbox_xpath).send_keys(text)
        self.driver.find_element(By.ID, self.search_btn_id).click()

    # def result_panel(self):
        # result = self.driver.find_element(By.ID, self.result_div_id)
        # result.find_element(By.TAG_NAME, "p").text ==
    def set_location(self, location):
        self.driver.find_element(By.ID, self.folder_drpmenu_id).click()
        if type == "all":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.all_msg_menuitem_id))
            ).click()
        elif type == "members":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.member_msg_menuitem_id))
            ).click()
        elif type == "eBay":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.eBay_msg_menuitem_id))
            ).click()
        elif type == "sent":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.sent_msg_menuitem_id))
            ).click()
        elif type == "trash":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.trash_msg_menuitem_id))
            ).click()
        elif type == "archive":
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.archive_msg_menuitem_id))
            ).click()
        else:  # FOLDER
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, self.folder_msg_menuitem_id))
            ).click()

    def adv_search_sender(self, input, location):
        self.driver.find_element(By.ID, self.advsearch_drpdown_id).click()
        self.driver.find_element(By.ID, self.searchby_sender_name_id).send_keys(input)
        self.set_location(location)
        self.driver.find_element(By.ID, self.advsearch_btn_id).click()

    def adv_search_subject(self, input, location):
        self.driver.find_element(By.ID, self.advsearch_drpdown_id).click()
        self.driver.find_element(By.ID, self.searchby_subject_id).send_keys(input)
        self.set_location(location)
        self.driver.find_element(By.ID, self.advsearch_btn_id).click()

    def adv_search_time(self, start, end, location):
        self.driver.find_element(By.ID, self.advsearch_drpdown_id).click()
        self.driver.find_element(By.ID, self.searchby_start_date_id).send_keys(start)
        self.driver.find_element(By.ID, self.searchby_end_date_id).send_keys(end)
        self.set_location(location)
        self.driver.find_element(By.ID, self.advsearch_btn_id).click()