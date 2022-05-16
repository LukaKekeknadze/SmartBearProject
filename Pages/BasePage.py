from driver import Driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(Driver):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by_locator, time_out=10):
        try:
            wait = WebDriverWait(self.driver, time_out)
            element = wait.until(EC.visibility_of_element_located((by_locator)))
            return element
        except Exception:
            raise Exception(
                'Element by "{0}" with the value "{1}" cannot be found.'.format(
                    by_locator[0], by_locator[1]
                )
            )