from selenium import webdriver
from selenium.webdriver.chrome.options import Options





class Driver:
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://smartbear.com//")
        driver.implicitly_wait(10)




