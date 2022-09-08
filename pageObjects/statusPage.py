from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class StatusPage(BasePage):
    statusCreate = (By.CLASS_NAME, 'hf-mod-create')
    statusCreateName = (By.XPATH, "//input[@data-test-id='form-field-name']")
    statusCreateDescription = (By.XPATH, "//textarea[@data-test-id='form-field-description']")
    statusBehaviourDropDown = (By.CLASS_NAME, "ember-basic-dropdown")
    statusBehaviourInput = (By.XPATH, "//input[@type='search']")
    statusSubmit = (By.XPATH, "//button[@data-test-id='add-status']")
    statusName = ReadConfig.getStatusName()
    statusDescription = ReadConfig.getStatusDescription()
    statusBehaviour = ReadConfig.getStatusBehaviour()
    statusMakeDefault = (
        By.XPATH, "//div[text()='" + statusName + "']//ancestor::td//following::a[text()='Make Default']")
    statusMakeDefaultConfirm = (By.XPATH, "//div[text()='" + statusName + "']//ancestor::td//following::div["
                                                                          "@data-test-id='default-status']")
    statusNameList = (By.XPATH, "//tr//div[text()='" + statusName + "']")
    statusDelete = (By.XPATH, "//a[text()='Delete']")
    statusDeleteConfirmationDropDown = (By.XPATH, "//span[text()='Choose Status']")
    statusDeleteConfirmationInputBox = (By.XPATH, "//input[@type='search']")
    statusDeleteConfirmationButton = (By.XPATH, "//button[text()='Delete']")
    statusDeleteConfirmation = (By.XPATH, """//div[text()='Status "' + statusName + '" is deleted successfully.']""")
    statusDeleteConfirmationReplace = ReadConfig.getStatusReplace()

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def create_status(self):
        self.click(self.statusCreate)
        self.enter_text(self.statusCreateName, self.statusName)
        self.enter_text(self.statusCreateDescription, self.statusDescription)
        self.click(self.statusSubmit)
        return self.verify_element_presence(self.statusNameList)

    def make_default(self):
        self.actions.move_to_element(self.statusNameList)
        self.actions.click(self.statusMakeDefault)
        self.actions.perform()
        return self.verify_element_presence(self.statusMakeDefaultConfirm)

    def delete_status(self):
        self.click(self.statusNameList)
        self.click(self.statusDelete)
        self.click(self.statusDeleteConfirmationButton)
        return self.verify_element_presence(self.statusDeleteConfirmation)
