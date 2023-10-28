from selenium import webdriver
from pages.main_page import MainPage
from pages.order_page import OrderPage
import allure


class TestGetOrderEntryPoints:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_header_order_button(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        main_page.go_main_page_by_link()
        main_page.click_order_header_button()
        title = order_page.get_first_order_page_title()

        assert title == 'Для кого самокат'

    def test_body_order_button(self):
        main_page = MainPage(self.driver)
        order_page = OrderPage(self.driver)

        main_page.go_main_page_by_link()
        main_page.click_order_body_button()
        title = order_page.get_first_order_page_title()

        assert title == 'Для кого самокат'

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
