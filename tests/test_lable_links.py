from selenium import webdriver
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.external_page import ExternalPage
from pages.order_page import OrderPage
import allure


class TestLogoLinks:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_logo_redirect_yandex(self):
        main_page = MainPage(self.driver)
        base_page = BasePage(self.driver)
        external_page = ExternalPage(self.driver)

        main_page.go_main_page_by_link()
        base_page.click_yandex_logo()
        dzen_link = external_page.get_link()

        assert dzen_link == 'https://dzen.ru/?yredirect=true'

    def test_logo_redirect_scooter(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)
        base_page = BasePage(self.driver)

        order_page.go_order_page()
        base_page.click_scooter_logo()
        main_page_link = main_page.get_link()

        assert main_page_link == 'https://qa-scooter.praktikum-services.ru/'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
