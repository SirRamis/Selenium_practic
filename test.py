import time

from locators import TITLE


def test_login(driver):
    actual_text = driver.find_element(*TITLE).text
    expected_text = "Products"
    assert actual_text == expected_text

    time.sleep(4)

