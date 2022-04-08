from selenium.webdriver.common.by import By
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_basket_button_exist(browser):
    browser.get(link)
    time.sleep(10)
    button = browser.find_elements(By.CLASS_NAME, 'btn-add-to-basket')
    assert button, "Basket button not found"
