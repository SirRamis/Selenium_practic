import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By

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


def test4_deleit_item(driver):
    driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="remove-sauce-labs-backpack"]').click()  # Удаляет с корзины
    assert not driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'


def test5_added_item_in_cart(driver):
    driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Добавляет в карзину из карточки
    time.sleep(2)
    assert driver.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине нет товаров'


def test6_deleit_item_in_cart():
    browser = webdriver.Chrome()
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()  # Логинится
    browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку
    time.sleep(2)
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Добавляет в карзину из карточки
    time.sleep(2)
    browser.find_element(By.XPATH,
                         '/html/body/div[1]/div/div/div[2]/div/div/div[2]/button').click()  # Удаляет с корзины через карточку товара

    assert not browser.find_elements(By.XPATH, '//*[@id="shopping_cart_container"]/a/span'), 'В корзине есть товары'

    time.sleep(4)
    browser.quit()


def test7_go_to_card():
    browser = webdriver.Chrome()
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()  # Логинится
    browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]').click()  # Проходит в карточку через картинку
    time.sleep(2)

    # select_element = browser.find_element('//*[@id="item_4_img_link"]')

    # Проверим, был ли элемент выбран
    # if select_element.is_selected():
    #     print("Элемент выбран")
    # else:
    #     print("Элемент не выбран")

    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', "Элемент не выбран"

    time.sleep(4)
    browser.quit()


def test8_go_to_card2(driver):
    browser.get('https://www.saucedemo.com/')
    browser.find_element(By.XPATH,
                         '//*[@id="item_4_title_link"]').click()  # переход к карточке товара после клика по названию товара
    assert browser.current_url == 'https://www.saucedemo.com/inventory-item.html?id=4', "Элемент не выбран"

    time.sleep(4)
    browser.quit()