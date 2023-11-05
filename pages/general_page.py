import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.external_page import ExternalPage
from pages.main_page import MainPage
from pages.base_page import BasePage


class GeneralPage(BasePage):
    YANDEX_LOGO = [By.XPATH, '//img[@src="/assets/ya.svg"]']  # Лого "Яндекс"
    SCOOTER_LOGO = [By.XPATH, '//img[@src="/assets/scooter.svg"]']  # Лого "Самокат"

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Кликаем на лого яндекса')
    def click_yandex_logo(self):
        self.click(self.YANDEX_LOGO)
        self.switch_page(1)
        self.wait(EC.presence_of_element_located, ExternalPage.DZEN_HEADER)

    @allure.step('Кликаем на лого самоката')
    def click_scooter_logo(self):
        self.click(self.SCOOTER_LOGO)
        self.wait(EC.presence_of_element_located, MainPage.SCOOTER_PIC)
