from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])

chrome_srvs = Service('C:\\Users\\s.tranin\\PycharmProjects\\Resource\\chromedriver.exe')
driver = webdriver.Chrome(options=options, service=chrome_srvs)