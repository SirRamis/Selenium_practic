import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from locators import USER_NAME, PASSWORD, LOGIN


@pytest.fixture
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--window-size=1440,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.saucedemo.com/')
    driver.find_element(*USER_NAME).send_keys('standard_user')
    driver.find_element(*PASSWORD).send_keys('secret_sauce')
    driver.find_element(*LOGIN).click()
    yield driver
    driver.quit()
