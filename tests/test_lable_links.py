from pages.main_page import MainPage
from pages.general_page import GeneralPage
from pages.external_page import ExternalPage
from pages.order_page import OrderPage


class TestLogoLinks:

    def test_logo_redirect_yandex(self, driver):
        main_page = MainPage(driver)
        general_page = GeneralPage(driver)
        external_page = ExternalPage(driver)

        main_page.go_main_page_by_link()
        general_page.click_yandex_logo()
        dzen_link = external_page.get_link()

        assert dzen_link == 'https://dzen.ru/?yredirect=true'

    def test_logo_redirect_scooter(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        general_page = GeneralPage(driver)

        order_page.go_order_page()
        general_page.click_scooter_logo()
        main_page_link = main_page.get_link()

        assert main_page_link == 'https://qa-scooter.praktikum-services.ru/'
