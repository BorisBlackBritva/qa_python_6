from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ExternalPage(BasePage):
    DZEN_HEADER = [By.XPATH, '//header[@id="dzen-header"]']

    def __init__(self, driver):
        super().__init__(driver)
