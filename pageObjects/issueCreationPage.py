import os

from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class UserIssueCreation(BasePage):
    issueSubject = (By.ID, "id_subject")
    issueMessage = (By.XPATH, "//div[@role='textbox']")
    issueAttachment = (By.ID, "attach-file-input")
    issueFullName = (By.ID, "id_name")
    issueEmail = (By.ID, "id_email")
    issueSubmit = (By.ID, "submit")
    subject = ReadConfig.getIssueSubject()
    message = ReadConfig.getIssueMessage()
    attachment = ReadConfig.getIssueAttachment()
    fullname = ReadConfig.getIssueFullName()
    email = ReadConfig.getIssueEmail()
    issueUrl = ReadConfig.getTicketUrl()
    issueCreateConfirm = (By.XPATH, "//div[contains(text(),'Your ticket has been created')]")

    def __init__(self, driver):
        super().__init__(driver)

    def createIssue(self):
        self.driver.execute_script(f'''window.open("{self.issueUrl}","_blank");''')
        self.enter_text(self.issueSubject, self.subject)
        self.enter_text(self.issueMessage, self.message)
        self.enter_text(self.issueAttachment, os.path.abspath('..\\Attachments\\sample.txt'))
        self.enter_text(self.issueFullName, self.fullname)
        self.enter_text(self.issueEmail, self.email)
        self.click(self.issueSubmit)
        return self.verify_element_presence(self.issueCreateConfirm)
