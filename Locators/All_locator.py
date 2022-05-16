from selenium.webdriver.common.by import By


class Locators():
    # cart icon locator
    cart_icon_id = (By.ID, "cart")

    # shop QA complete
    shop_qa_CLASS = (By.CSS_SELECTOR, '#form > div.sb-legacy > div.store-content > div.container-wrap.home-tail > div > div > div:nth-child(3) > a')

    # license lists
    license_xpath = (By.XPATH, '//*[@id="Buy"]/div/div[1]/div[1]/div[2]/div')

    # SaaS location
    SaaS_license_xpath = (By.XPATH, '//*[@id="Buy"]/div/div[1]/div[1]/div[2]/div/div/div/ul/li[2]/a')

    # Subtotal price
    TotalPrice_xpath = (By.XPATH, '//*[@id="subtotal-Buy"]')

    # add to cart button
    add_cart_item_xpath = (By.XPATH, '//*[@id="subtotal-link-Buy"]')

    # license check
    check_license_xpath = (By.XPATH, '//*[@id="form"]/div[5]/div[1]/div[2]/div/div/div[3]/div[1]/div[3]')

    # price check
    check_price_id = (By.ID, 'cart-total-price')
