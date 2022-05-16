from Locators.All_locator import Locators
from Pages.BasePage import BasePage
import allure


class QA_button(BasePage):
    def __init__(self):
        pass

    @allure.step("click cart icon")
    def click_qa_complete_button(self):
        qa_button = BasePage.find_element(self,Locators.shop_qa_CLASS)
        qa_button.click()
        return qa_button