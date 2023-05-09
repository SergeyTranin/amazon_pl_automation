from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

from utilities.logger import Logger


class ProductPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    gear_number = "//span[text()='27']"
    wheel_size = "//span[text()='26 cali']"
    frame_type = "//span[text()='Aluminium']"
    seller = "//span[text()='Flying together']"
    product_link = "//span[text()='Rowery górskie Składany 26 cali, Fat Tiremountain Trail Bike, rama ze stali wysokowęglowej Podwójny rower z hamulcem tarczowym, 21/24/27 prędkości, B-21 prędkości']"
    product_title = "//span[text()='        Rowery górskie Składany 26 cali, Fat Tiremountain Trail Bike, rama ze stali wysokowęglowej Podwójny rower z hamulcem tarczowym, 21/24/27 prędkości, B-21 prędkości       ']"
    product_title_text = "        Rowery górskie Składany 26 cali, Fat Tiremountain Trail Bike, rama ze stali wysokowęglowej Podwójny rower z hamulcem tarczowym, 21/24/27 prędkości, B-21 prędkości       "
    add_to_cart_button = "//input[@id='add-to-cart-button']"
    #confirm_add_to_cart = "//span[text()=' Dodano do koszyka']"
    go_to_cart_button = "//span[@id='nav-cart-count']"
    cart_prod_title = "//span[text()='Rowery górskie Składany 26 cali, Fat Tiremountain Trail Bike, rama ze stali wysokowęglowej Podwójny rower z hamulcem tarczowym, 21/…']"
    cart_prod_text = "Rowery górskie Składany 26 cali, Fat Tiremountain Trail Bike, rama ze stali wysokowęglowej Podwójny rower z hamulcem tarczowym, 21/…"

    """Getters"""

    def get_gear_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.gear_number)))

    def get_wheel_size(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.wheel_size)))

    def get_frame_type(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.frame_type)))

    def get_seller(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.seller)))

    def get_product_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_link)))

    def get_product_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))

    def get_cart_prod_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cart_prod_title)))

    """Actions"""

    def click_gear_number(self):
        self.get_gear_number().click()
        print("Select gear number")

    def click_wheel_size(self):
        self.get_wheel_size().click()
        print("Select wheel size")

    def click_frame_type(self):
        self.get_frame_type().click()
        print("Select frame type")

    def click_seller(self):
        self.get_seller().click()
        print("Select seller")

    def click_product_link(self):
        self.get_product_link().click()
        print("Select product")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Add product to cart")

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print("Go to cart")

    """Methods"""

    def apply_filters(self):
        Logger.add_start_step(method='apply_filters')
        self.get_current_url()
        self.click_gear_number()
        self.click_wheel_size()
        self.click_frame_type()
        self.click_seller()
        self.click_product_link()
        self.get_screenshot()
        self.click_add_to_cart_button()
        self.click_go_to_cart_button()
        self.get_screenshot()
        self.assert_url("https://www.amazon.pl/gp/cart/view.html?ref_=nav_top_cart")
        Logger.add_end_step(url=self.driver.current_url, method='apply_filters')