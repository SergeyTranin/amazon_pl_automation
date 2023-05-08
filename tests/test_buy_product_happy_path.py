from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from pages.home_page import HomePage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    chrome_srvs = Service('C:\\Users\\s.tranin\\PycharmProjects\\Resource\\chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=chrome_srvs)

    print("Start 'Buy product' test")

    hp = HomePage(driver)
    hp.open_catalog()

    pp = ProductPage(driver)
    pp.apply_filters()

    cp = CartPage(driver)
    cp.proceed_to_payment()
    print("Smoke test passed")

    time.sleep(3)
    driver.close()