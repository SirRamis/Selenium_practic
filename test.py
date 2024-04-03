import time

USER_NAME = ('xpath', '//*[@id="user-name"]')
PASSWORD = ('xpath', '//*[@id="password"]')
LOGIN = ('xpath', '//*[@id="login-button"]')
TITLE = ('xpath', '//*[@id="header_container"]/div[2]/span')

def test_login(driver):
    actual_text = driver.find_element(*TITLE).text
    expected_text = "Products"
    assert actual_text == expected_text

    time.sleep(4)

