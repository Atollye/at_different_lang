import time

from selenium.webdriver.common.by import By


class TestStandardPurchase():

    def test_add_item_to_the_cart_button(self, browser):
        browser.get(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        )
        buttons = browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")
        buttons_number = len(buttons)
        assert buttons_number > 0, (
            "There is no 'Add to basket' button on the page"
        )
        assert buttons_number == 1, (
            "There are more than one 'Add to basket' button on the page"
        )
        time.sleep(5)
