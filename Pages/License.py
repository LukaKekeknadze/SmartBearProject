from Locators.All_locator import Locators
from Pages.BasePage import BasePage
import allure


class LICENSE(BasePage):
    def __init__(self):
        pass

    @allure.step("Choose License")
    def click_license_dropdown(self):
        choose_license = BasePage.find_element(self,Locators.license_xpath)
        choose_license.click()
        return choose_license

    @allure.step("Choose SaaS License")
    def Choose_SaaS_License(self):
        choose_SaaS_license = BasePage.find_element(self,Locators.SaaS_license_xpath)
        choose_SaaS_license.click()
        return choose_SaaS_license

    @allure.step("Check price")
    def check_price(self):
        check_price = BasePage.find_element(self, Locators.TotalPrice_xpath)
        return check_price.text

    @allure.step("add license to cart")
    def add_button(self):
        add_to_cart_button = BasePage.find_element(self, Locators.add_cart_item_xpath)
        add_to_cart_button.click()
        return add_to_cart_button