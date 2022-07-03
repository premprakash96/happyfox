from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class PriorityPage(BasePage):
    priorityCreate = (By.CLASS_NAME, 'hf-mod-create')
    priorityCreateName = (By.XPATH, "//input[@data-test-id='form-field-name']")
    priorityCreateDescription = (By.XPATH, "//input[@data-test-id='form-field-description']")
    priorityCreateHelp = (By.XPATH, "//input[@data-test-id='form-field-helpText']")
    prioritySubmit = (By.XPATH, "//input[@data-test-id='add-priority']")
    priorityName = ReadConfig.getPriorityName()
    priorityDescription = ReadConfig.getPriorityDescription()
    priorityMakeDefault = (By.XPATH, "//tr//span[text()='" + priorityName + "']//ancestor::td//following::div["
                                                                            "contains(text(),'Make Default')]")
    priorityMakeDefaultConfirm = (By.XPATH, "//tr//span[text()='" + priorityName + "']//ancestor::td//following::div[@data-test-id='default-priority']")
    priorityNameList = (By.XPATH, "//tr//span[text()='" + priorityName + "']")
    priorityDelete = (By.XPATH, "//a[text()='Delete']")
    priorityDeleteConfirmationDropDown = (By.XPATH, "//span[text()='Choose Priority']")
    priorityDeleteConfirmationInputBox = (By.XPATH, "//input[@type='search']")
    priorityDeleteConfirmationButton = (By.XPATH, "//button[text()='Delete']")
    priorityDeleteConfirmation = (By.XPATH, "//div[text()='Priority '" + priorityName + "' is deleted successfully.']")

    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def create_priority(self):
        self.click(self.priorityCreate)
        self.enter_text(self.priorityCreateName, self.priorityName)
        self.enter_text(self.priorityCreateDescription, self.priorityDescription)
        self.click(self.prioritySubmit)
        return self.verify_element_presence(self.priorityNameList)

    def make_default(self):
        self.actions.move_to_element(self.priorityNameList)
        self.actions.click(self.priorityMakeDefault)
        self.actions.click()
        return self.verify_element_presence(self.priorityMakeDefaultConfirm)

    def delete_priority(self):
        self.click(self.priorityNameList)
        self.click(self.priorityDelete)
        # self.click(self.priorityDeleteConfirmationDropDown)
        # self.enter_text(self.priorityDeleteConfirmationInputBox, self.priorityDeleteConfirmationReplace + Keys.RETURN)
        self.click(self.priorityDeleteConfirmationButton)
        return self.verify_element_presence(self.priorityDeleteConfirmation)
