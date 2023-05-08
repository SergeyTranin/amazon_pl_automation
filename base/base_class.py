import datetime

class Base:
    def __init__(self, driver):
        self.driver = driver

    """Get current URL method"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    """Assert URL method"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("URL assertion passed")

    """Assert text method"""

    def assert_text(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Text assertion passed")

    """Screenshot method"""

    def get_screenshot(self):
        current_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = f"screenshot_{current_date}.png"
        self.driver.save_screenshot(f"C:\\Users\\s.tranin\\PycharmProjects\\amazon_pl_automation\\screenshots\\{name_screenshot}")
