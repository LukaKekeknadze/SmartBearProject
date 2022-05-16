from pytest import assume
import allure
from Pages.HomePage import HomePage
from Pages.QAcompletePage import QA_button
from Pages.License import LICENSE
from Pages.CartPage import Cart

HP = HomePage()
QA = QA_button()
LC = LICENSE()
CR = Cart()


@allure.feature("SmartBear Test Automation Add Item To Cart")
@allure.story("FinalProject")
class Test_SmartBear:
    @allure.title("click cart icon")
    @allure.description("go to site and click icon")
    def test_click_cart_icon(self):
        HP.click_cart_icon()

    @allure.title("click cart shopQA button")
    @allure.description("go to site and shop QAcomplete")
    def test_click_qa_complete_button(self):
        QA.click_qa_complete_button()

    @allure.title("choose license")
    @allure.description("Choose license")
    def test_choose_license(self):
        LC.click_license_dropdown()

    @allure.title("choose SaaS license")
    @allure.description("Choose license Saas")
    def test_choose_SaaS_license(self):
        LC.Choose_SaaS_License()

    @allure.title("check subtotal price")
    @allure.description("Price")
    def test_check_price(self):
        tot_price = LC.check_price()
        with assume:
            assert "€679" in tot_price

    @allure.title("add to cart item")
    @allure.description("add to cart item")
    def test_add_to_cart(self):
        LC.add_button()

    @allure.title("check licence in the cart")
    @allure.description("check licence in the cart")
    def test_check_lic(self):
        license_ = CR.check_lic()
        with assume:
            assert "1 Year" in license_

    @allure.title("check license price the cart")
    @allure.description("###")
    def test_check_price_in_cart(self):
        ch_prc = CR.check_price_in_cart()
        with assume:
            assert "€679" in ch_prc

