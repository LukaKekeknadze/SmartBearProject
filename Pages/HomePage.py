from Locators.All_locator import Locators
from Pages.BasePage import BasePage
import allure


class HomePage(BasePage):
    def __init__(self):
        pass

    @allure.step("click cart icon")
    def click_cart_icon(self):
        cart_page = BasePage.find_element(self,Locators.cart_icon_id)
        cart_page.click()
        return cart_page