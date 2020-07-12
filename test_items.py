from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    # time.sleep(30)
    wait = WebDriverWait(browser, 10)
    try:
        wait.until(EC.visibility_of_element_located(
                  (By.CSS_SELECTOR, ".add-to-basket")))
    except (NoSuchElementException, TimeoutException):
        assert False, "No add-to-basket button"
