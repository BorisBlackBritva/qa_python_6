from selenium.webdriver.common.by import By


class ExternalPage:
    DZEN_HEADER = [By.XPATH, '//header[@id="dzen-header"]']

    def __init__(self, driver):
        self.driver = driver

    def get_link(self):
        return self.driver.current_url
