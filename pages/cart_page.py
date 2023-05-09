from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

from utilities.logger import Logger


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    proceed_to_retail = "//input[@name='proceedToRetailCheckout']"

    """Getters"""

    def get_proceed_to_retail(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.proceed_to_retail)))

    """Actions"""

    def click_proceed_to_retail(self):
        self.get_proceed_to_retail().click()
        print("Click on proceed button")


    """Methods"""

    def proceed_to_payment(self):
        Logger.add_start_step(method='proceed_to_payment')
        self.get_current_url()
        self.click_proceed_to_retail()
        self.get_screenshot()
        Logger.add_end_step(url=self.driver.current_url, method='proceed_to_payment')