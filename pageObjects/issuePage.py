import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pageObjects.basePage import BasePage
from utilities.readProperties import ReadConfig


class IssuePage(BasePage):
    priority = ReadConfig.getPriorityName()
    status = ReadConfig.getStatusName()
    issueStatus = (By.CLASS_NAME, 'hf-ticket-status_name')
    issuePriority = (By.XPATH, "//article//div[@data-test-id='ticket-box_priority']")
    issueReply = (By.XPATH, "//span[text()='Reply']")
    issueClickCannedAction = (By.XPATH, "//div[@data-test-id='add-update-editor']//span[text()='Canned Action']")
    issueCannedActionApply = (By.XPATH, "//button[text()='Apply']")
    issueReplyCannedActionName = ReadConfig.getIssueReplyCannedAction()
    issueReplyStatus = ReadConfig.getIssueReplyStatus()
    issueReplyPriority = ReadConfig.getIssueReplyPriority()
    issueReplytags = ReadConfig.getIssueReplyTags()
    issueCannedActionContainer = (By.XPATH, "div[class='hf-canned-action-list ']")
    issueCannedAction = (By.XPATH, "//li[text()='" + issueReplyCannedActionName + "']")
    issueCannedActionStatus = (By.XPATH, "//div[@data-test-id='add-update-editor']//div[@data-test-id='ticket-box_status']")
    issueCannedActionPriority = (By.XPATH, "//div[@data-test-id='add-update-editor']//div[@data-test-id='ticket-box_priority']")
    issueCannedActionTagsEdit = (By.XPATH, "//div[@data-test-id='editor-add-tags-trigger']")
    issueCannedActionTagsList = (By.XPATH, "//div[contains(@class,'hf-mod-edit-tags-section')]//li")
    issueAddReply = (By.XPATH, "//button[text()='Add Reply']")
    # issueFloatingBar = (By.XPATH, "//div[@data-test-id='ticket-details-minimized-update']")
    # issueFloatingBarMinimize = (By.XPATH, "//div[@data-test-id='ticket-details-minimized-update']//div[@class='hf-floating-editor_minimized-draft_maximize-button']")


    def __init__(self, driver):
        super().__init__(driver)
        self.actions = ActionChains(driver)

    def choose_canned_action(self):
        self.scroll_element(self.issueCannedActionContainer, 100)
        self.click(self.issueClickCannedAction)

    def choose_reply_message(self):
        self.click(self.issueReply)
        self.click(self.issueClickCannedAction)
        self.choose_canned_action()
        self.click(self.issueCannedActionApply)
        new_status = self.verify_element_presence_and_return_text(self.issueCannedActionStatus)
        new_priority = self.verify_element_presence_and_return_text(self.issueCannedActionPriority)
        self.click(self.issueCannedActionTagsEdit)
        new_tags = self.verify_all_elements_presence_and_return_text(self.issueCannedActionTagsList)
        return new_status, new_priority, new_tags

    def verify_status(self):
        if self.verify_element_presence_and_return_text(self.issueStatus) is self.status:
            return True
        return False

    def verify_priority(self):
        if self.verify_element_presence_and_return_text(self.issuePriority) is self.priority:
            return True
        return False
