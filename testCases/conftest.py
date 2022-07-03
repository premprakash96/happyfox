import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys


@pytest.fixture()
def setup(request, browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r"C:\\Users\\pmanicka\\Downloads\\chromedriver_win32 (2)\chromedriver.exe")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser == 'firefox':
        pass
    else:
        pass
    request.cls.driver = driver
    yield
    driver.close()


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
