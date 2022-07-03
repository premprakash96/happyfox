from selenium import webdriver
from selenium.webdriver.common.by import By

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
    captchaCheck = (By.CLASS_NAME, 'recaptcha-checkbox-checked')
    captchaContainer = (By.ID, 'recaptcha-anchor')

    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.driver.get(self.url)
        if self.get_title('Login'):
            print("Username is " + self.user_id)
            print("Password is " + self.user_pass)
            self.enter_text(self.username, self.user_id)
            self.enter_text(self.password, self.password)
            self.click(self.submit)
            if self.check_captcha():
                self.click_captcha()
            return True if self.get_title('View Tickets') else False

    def check_captcha(self):
        if self.verify_element_presence(self.captcha):
            return True
        return False

    def click_captcha(self):
        self.click(self.captcha)
        try:
            element = self.driver.find_element(self.captchaContainer)
            if self.captchaCheck in element.get_attribute("class"):
                return True
            else:
                return False
        except TimeoutError as e:
            return False
