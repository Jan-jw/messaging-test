from selenium.webdriver.common.by import By
# from selenium import webdriver
class LoginPage:

    signin_page_linktxt = "Sign in"
    username_txt_id = "userid"
    cont_btn_xpath = "//button[@id='signin-continue-btn']"
    # register_linktxt = "create an account"
    # mobile_login_btn_id = "switch-to-mobile-link"

    password_txt_id = "pass"
    signin_btn_id = "sgnBt"
    # switch_user_linktxt = "Switch account"
    # # logout_linktxt = "Log Out"
    # forgot_linktxt = "Need help signing in?"
    # otp_login_btn_id = "idf-otp-btn"
    # reset_pass_btn_id = "fyp-btn"
    #
    # stay_signin_cbx_xpath = "//input[@id='kmsi-checkbox']"
    # stay_signin_cbx_xpath = "//input[@id='kmsi-checkbox']"

    # CHANGE TO DRIVER
    def __init__(self, browser):
        self.browser = browser

    def signin_page(self):
        self.browser.find_element(By.LINK_TEXT, self.signin_page_linktxt).click()

    def set_username(self, username):
        self.browser.find_element(By.ID, self.username_txt_id).clear()
        self.browser.find_element(By.ID, self.username_txt_id).send_keys(username)

    def set_password(self, password):
        self.browser.find_element(By.ID, self.password_txt_id).clear()
        self.browser.find_element(By.ID, self.password_txt_id).send_keys(password)

    def click_cont (self):
        self.browser.find_element(By.XPATH, self.cont_btn_xpath).click()

    # def click_forgot (self):
    #     self.browser.find_element(By.LINK_TEXT, self.forgot_linktxt).click()

    def click_signin (self):
        self.browser.find_element(By.ID, self.signin_btn_id).click()

    # def click_logout (self):
    #     self.browser.find_element(By.LINK_TEXT, self.logout_linktxt).click()


