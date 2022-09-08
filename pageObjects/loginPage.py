import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class LoginPage(BasePage):
    username = (By.ID, 'id_username')
    password = (By.ID, 'id_password')
    submit = (By.ID, 'btn-submit')
    user_id = ReadConfig.getUsername()
    user_pass = ReadConfig.getPassword()
    url = ReadConfig.getAgentUrl()
    captcha = (By.CLASS_NAME, 'recaptcha-checkbox-spinner')
    captchaCheck = 'recaptcha-checkbox-checked'
    captchaFrame = (By.XPATH, "//iframe(@title='reCAPTCHA')")
    captchaContainer = (By.ID, 'recaptcha-anchor')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.get(self.url)
        if self.get_title('Login'):
            print("Username is " + self.user_id)
            print("Password is " + self.user_pass)
            # self.enter_text(self.username, self.user_id)
            # self.enter_text(self.password, self.password)
            self.enter_text(self.username, 'Agent1')
            self.enter_text(self.password, 'Agent@123')
            self.click(self.submit)
            if self.check_captcha():
                self.click_captcha()
            return True if self.get_title('View Tickets') else False

    def check_captcha(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.frame_to_be_available_and_switch_to_it(self.captchaFrame))
            return True
        except TimeoutException as e:
            return False

    def click_captcha(self):
        self.click(self.captcha)
        if self.driver.find_element(self.captchaContainer).is_selected():
            print("Captcha selected")
            return True
        print("Captcha not selected")
        return False
        # try:
        #     element = self.driver.find_element(self.captchaContainer)
        #     if self.captchaCheck in element.get_attribute("class"):
        #         return True
        #     else:
        #         return False
        # except TimeoutError as e:
        #     return False
