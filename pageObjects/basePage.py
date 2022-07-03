import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def enter_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_title(self, title):
        try:
            WebDriverWait(self.driver, 10).until(EC.title_contains(title))
            return self.driver.title
        except TimeoutException as e:
            print("Element not found and had a timeout exception")
            return False

    def click_from_menu(self, locator):
        self.click((By.CLASS_NAME, 'hf-top-bar-title'))
        self.click(locator)

    def verify_element_presence(self, locator, duration=10):
        try:
            element = WebDriverWait(self.driver, duration).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException as e:
            print("Element not found and had a timeout exception")
            return False

    def verify_element_presence_and_return_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException as e:
            print("Element not found and had a timeout exception")
            return False

    def verify_all_elements_presence_and_return_text(self, locator):
        texts = []
        try:
            elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
            for element in elements:
                texts.append(element.text)
            return texts
        except TimeoutException as e:
            print("Element not found and had a timeout exception")
            return False

    def scroll_element(self, locator, vertical_coordinate):
        element = self.driver.find_element_by_xpath(locator)
        for i in range(0, 50):
            self.driver.execute_script("arguments[0].scrollTop = arguments[1]", element, vertical_coordinate)
            vertical_coordinate += 100
            time.sleep(1)

    def switch_to_previous_window(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
