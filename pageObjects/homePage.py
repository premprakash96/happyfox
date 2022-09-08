from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class HomePage(BasePage):
    account = (By.XPATH, "//div[@data-test-id='staff-menu']")
    logout = (By.XPATH, "//li[@data-test-id='staff-menu-logout']")
    name = ReadConfig.getIssueSubject()
    issueName = (By.XPATH, "//a[text()='" + name + "']")
    # status = (By.XPATH, "//li[@data-test-id='module-switcher_manage-statuses']")
    status = (By.XPATH, "//a[text()='Statuses']")
    priority = (By.XPATH, "//a[text()='Priorities']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_issue(self):
        self.click(self.issueName)
        return True if self.get_title(self.name) == self.name else False

    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text

    def logout_page(self):
        self.click(self.account)
        self.click(self.logout)
        return True if self.get_title('Login') else False
