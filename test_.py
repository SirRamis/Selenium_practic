import time

import driver as driver

from locators import TITLE, ADDITEM_BUTTON, ITEMINCART_FIELD
from conftest import driver

def test_login(driver):
    actual_text = driver.find_element(*TITLE).text
    expected_text = "Products"
    assert actual_text == expected_text
    time.sleep(4)

def test_add_item(driver):
    driver.find_element(*ADDITEM_BUTTON).click()
    actual_text = driver.find_element(*ITEMINCART_FIELD).text
    assert actual_text
