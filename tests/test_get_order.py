import pytest
from pages.order_page import OrderPage


class TestGetOrderEntryPoints:
    CREDS1 = OrderPage.FIRST_FORM_DATA
    CREDS2 = OrderPage.SECOND_FORM_DATA

    def test_get_order_important_fields(self, driver):
        order_page = OrderPage(driver)
        name = self.CREDS1['name'][0]
        surname = self.CREDS1['surname'][0]
        address = self.CREDS1['address'][0]
        metro_station = self.CREDS1['metro_station'][0]
        tel_number = self.CREDS1['tel_number'][0]
        delivery_date = self.CREDS2['delivery_date'][0]
        term_value = self.CREDS2['rent_term'][0]

        order_page.go_order_page()
        order_page.enter_name(name)
        order_page.enter_surname(surname)
        order_page.enter_address(address)
        order_page.choose_metro_station_value_via_list(metro_station)
        order_page.enter_tel_number(tel_number)
        order_page.click_continue()

        order_page.choose_delivery_date_via_datepicker(delivery_date)
        order_page.choose_term_value(term_value)
        order_page.complete_order()
        order_page.confirm_order()

        assert 'Заказ оформлен' in order_page.get_order_info_title_text()

    @pytest.mark.parametrize(
        'name, surname, address, metro_station, tel_number, delivery_date, term_value, scooter_color, comment', [
            [CREDS1['name'][0], CREDS1['surname'][0], CREDS1['address'][0], CREDS1['metro_station'][0],
             CREDS1['tel_number'][0],
             CREDS2['delivery_date'][0], CREDS2['rent_term'][0], CREDS2['scooter_color'][0], CREDS2['comment'][0]],
            [CREDS1['name'][1], CREDS1['surname'][1], CREDS1['address'][1], CREDS1['metro_station'][1],
             CREDS1['tel_number'][1], CREDS2['delivery_date'][1], CREDS2['rent_term'][1], CREDS2['scooter_color'][1],
             CREDS2['comment'][1]]

        ])
    def test_get_order_all_fields(self, name, surname, address, metro_station,
                                  tel_number, delivery_date, term_value, scooter_color, comment, driver):
        order_page = OrderPage(driver)

        order_page.go_order_page()
        order_page.enter_name(name)
        order_page.enter_surname(surname)
        order_page.enter_address(address)
        order_page.choose_metro_station_value_via_type(metro_station)
        order_page.enter_tel_number(tel_number)
        order_page.click_continue()

        order_page.choose_delivery_date_via_type(delivery_date)
        order_page.choose_term_value(term_value)
        order_page.choose_scooter_color(scooter_color)
        order_page.enter_comment(comment)
        order_page.complete_order()
        order_page.confirm_order()

        assert 'Заказ оформлен' in order_page.get_order_info_title_text()
