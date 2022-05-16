from Locators.All_locator import Locators
from Pages.BasePage import BasePage
import allure


class Cart(BasePage):
    def __init__(self):
        pass

    @allure.step("check license in the cart")
    def check_lic(self):
        cart_Lic = BasePage.find_element(self, Locators.check_license_xpath)
        return cart_Lic.text

    @allure.step("check price in the cart")
    def check_price_in_cart(self):
        lic_pric = BasePage.find_element(self, Locators.check_price_id)
        return lic_pric.text