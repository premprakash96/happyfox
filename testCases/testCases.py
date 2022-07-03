import pytest
from selenium import webdriver

from pageObjects import homePage, issuePage, issueCreationPage, loginPage, priorityPage, statusPage


@pytest.mark.usefixtures("setup")
class TestScenarios:
    def test_scenario1_3(self):
        self.lp = loginPage.LoginPage(self.driver)
        self.hp = homePage.HomePage(self.driver)
        self.sp = statusPage.StatusPage(self.driver)
        self.pp = priorityPage.PriorityPage(self.driver)
        assert self.lp.login() is True
        self.hp.click_from_menu(self.hp.status)
        assert self.sp.create_status() is True
        assert self.sp.delete_status() is True
        self.hp.click_from_menu(self.hp.priority)
        assert self.pp.create_priority() is True
        assert self.pp.delete_priority() is True

    def test_scenario1_2_3(self):
        self.lp = loginPage.LoginPage(self.driver)
        self.hp = homePage.HomePage(self.driver)
        self.sp = statusPage.StatusPage(self.driver)
        self.pp = priorityPage.PriorityPage(self.driver)
        self.icp = issueCreationPage.UserIssueCreation(self.driver)
        self.ip = issuePage.IssuePage(self.driver)
        assert self.lp.login() is True
        self.hp.click_from_menu(self.hp.status)
        assert self.sp.create_status() is True
        assert self.sp.make_default() is True
        self.hp.click_from_menu(self.hp.priority)
        assert self.pp.create_priority() is True
        assert self.pp.make_default() is True
        assert self.icp.createIssue() is True
        self.hp.switch_to_previous_window()
        assert self.hp.click_issue() is True
        assert self.ip.verify_priority() is True
        assert self.ip.verify_status() is True
        status, priority, tags = self.ip.choose_reply_message()
        assert status is self.ip.issueStatus
        assert priority is self.ip.issuePriority
        assert self.ip.issueReplytags in tags
        self.hp.click_from_menu(self.hp.status)
        assert self.sp.delete_status() is True
        self.hp.click_from_menu(self.hp.priority)
        assert self.pp.delete_priority() is True
        assert self.hp.logout_page() is True
