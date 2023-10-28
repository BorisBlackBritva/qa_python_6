from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.external_page import ExternalPage
from pages.main_page import MainPage


class BasePage:
    YANDEX_LOGO = [By.XPATH, '//img[@src="/assets/ya.svg"]']  # Лого "Яндекс"
    SCOOTER_LOGO = [By.XPATH, '//img[@src="/assets/scooter.svg"]']  # Лого "Самокат"

    def __init__(self, driver):
        self.driver = driver

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()
        tab_handles = self.driver.window_handles
        self.driver.switch_to.window(tab_handles[1])
        WebDriverWait(self.driver, 7).until(EC.presence_of_element_located(ExternalPage.DZEN_HEADER))

    def click_scooter_logo(self):
        self.driver.find_element(*self.SCOOTER_LOGO).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(MainPage.SCOOTER_PIC))

    def get_link(self):
        return self.driver.current_url
