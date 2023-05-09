from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
import time

from utilities.logger import Logger


class HomePage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """URL address"""
    url = 'https://www.amazon.pl'

    """Locators"""

    #accept_cookies = "//input[@id='sp-cc-accept']"
    reject_coockies = "//a[text()='Kontynuuj bez akceptacji']"
    logo_button = "//a[@id = 'nav-bb-logo']"
    burger_menu_button = "//span[@class = 'hm-icon-label']"
    sport_menu_item = "//a[@data-menu-id='12']"
    cycling_category = "//a[@href='/gp/browse.html?node=20859834031&ref_=nav_em_sp_cycle_0_2_12_13']"
    cycling_link = "https://www.amazon.pl/gp/browse.html?node=20859834031&ref_=nav_em_sp_cycle_0_2_12_13"
    cycling_page_banner = "//div[@class = 'fst-h1-st pageBanner']"
    bicycles_item = "//a[@title='Rowery']"
    bicycles_page_banner = "//div[@class='fst-h1-st pageBanner']"
    mtb = "//span[text()='Rowery górskie']"
    mtb_page_banner = "//div[@class='fst-h1-st pageBanner']"

    """Getters"""

    # def get_cookies_button(self):
    #     return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accept_cookies)))

    def get_reject_cookies_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.reject_coockies)))

    def get_logo_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.logo_button)))

    def get_burger_menu_button(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.burger_menu_button)))

    def get_sport_menu_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.sport_menu_item)))

    def get_cycling_category(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cycling_category)))

    def get_cycling_page_banner(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.cycling_page_banner)))

    def get_bicycles_item(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.bicycles_item)))

    def get_bicycles_page_banner(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.bicycles_page_banner)))

    def get_mountain_bikes(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mtb)))

    def get_mtb_page_banner(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mtb_page_banner)))

    """Actions"""

    def click_reject_cookies_button(self):
        self.get_reject_cookies_button().click()
        print("Click on 'Reject cookies' button")

    # def click_accept_cookies_button(self):
    #     self.get_cookies_button().click()
    #     print("Click on 'Accept cookies' button")

    def click_logo_button(self):
        self.get_logo_button().click()
        print("Click on logo button")

    def click_burger_menu_button(self):
        self.get_burger_menu_button().click()
        time.sleep(2)
        print("Click on burger menu button")

    def click_sport_menu_item(self):
        self.get_sport_menu_item().click()
        time.sleep(2)
        print("Click on sport menu item")

    def click_cycling_category(self):
        self.get_cycling_category().click()
        print("Click on Cycling category")

    def click_bicycles_item(self):
        self.get_bicycles_item().click()
        print("Click on Bicycles item")

    def click_mountain_bikes(self):
        self.get_mountain_bikes().click()
        print("Select mountain bikes")

    """Methods"""

    def open_catalog(self):
        Logger.add_start_step(method='open_catalog')
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        time.sleep(10)
        self.click_reject_cookies_button()
        #self.click_logo_button()
        self.click_burger_menu_button()
        time.sleep(1)
        self.click_sport_menu_item()
        self.click_cycling_category()
        self.assert_text(self.get_cycling_page_banner(), "Kolarstwo")
        self.click_bicycles_item()
        self.assert_text(self.get_bicycles_page_banner(), "Kolarstwo - Rowery")
        self.click_mountain_bikes()
        self.assert_text(self.get_mtb_page_banner(), "Kolarstwo - Rowery górskie")
        Logger.add_end_step(url=self.driver.current_url, method='open_catalog')
