import datetime
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage():
    # Страница с формой 1
    ORDER_PAGE_URL = 'https://qa-scooter.praktikum-services.ru/order'
    FIRST_FORM_PAGE_TITLE = [By.XPATH, '//div[text()="Для кого самокат"]']  # Титул первой страницы заказа
    FIRST_FORM_CONTINUE_BUTTON = [By.XPATH, '//button[text()="Далее"]']  # Кнопка "Далее"
    FIRST_FORM_CONTINUE_ORDER_BUTTON = [By.XPATH, '//button[text()="Далее"]']  # Кнопка "Заказать"

    # Поля формы 1
    NAME_FIELD = [By.XPATH, '//input[@placeholder="* Имя"]']  # Поле "Имя"
    SURNAME_FIELD = [By.XPATH, '//input[@placeholder="* Фамилия"]']  # Поле "Фамилия"
    ADDRESS_FIELD = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]']  # Поле "Адрес"
    METRO_STATION_FIELD = [By.XPATH, '//input[@placeholder="* Станция метро"]']  # Поле "Станция метро"
    METRO_STATION_LIST = [By.XPATH, '//ul[@class="select-search__options"]']  # Список станций
    METRO_STATION_VALUE = lambda self, station_name: [By.XPATH, f'//div[text()="{station_name}"]']
    TEL_NUM_FIELD = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]']  # Поле "Телефон"

    # Данные для заказа: Форма 1
    FIRST_FORM_DATA = {
        'name': ['Эд', 'Эдуардищеееееее'],
        'surname': ['Ро', 'Творожековскиий'],
        'address': ['Место', 'Днищевоподмостовогрязеречногоуховолосатогокосохер'],
        'metro_station': ['ВДНХ', 'Библиотека имени Ленина'],
        'tel_number': ['89999999999', '+78888888888']
    }

    # Страница с формой 2
    SECOND_FORM_PAGE_TITLE = [By.XPATH, '//div[text()="Про аренду"]']  # Титул второй страницы заказа
    SECOND_FORM_COMPLETE_ORDER_BUTTON = [By.XPATH, '//div[starts-with(@class, "Order_Buttons")]/button[text()="Заказать"]']  # Кнопка "Заказать"
    # Дата пикер
    CURRENT_MONTH = [By.CLASS_NAME, 'react-datepicker__current-month']  # Текущий месяц в датапикере
    DAY = lambda self, current_month_and_year, day: [By.XPATH, f'//div[text()="{day}" and '
                                                                       f'contains(@aria-label, "{current_month_and_year}")]']  # День в датапикере
    NEXT_MONTH_BUTTON = [By.XPATH, '//button[text()="Next Month"]']  # Кнопка переключения на след. месяц


    # Поля формы 2
    DELIVERY_DATE_FIELD = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]']  # Поле "Когда привезти самокат"
    RENT_TERM_FIELD = [By.XPATH, '//div[text()="* Срок аренды"]']  # Поле "Срок аренды"
    RENT_TERM_VALUE = lambda self, term: [By.XPATH, f'//div[text()="{term}"]']  # Значение в списке
    SCOOTER_COLOR_VALUE = lambda self, color: [By.XPATH, f'//label[@for="{color}"]']  # Поле "Цвет самоката"
    COMMENT_FIELD = [By.XPATH, '//input[@placeholder="Комментарий для курьера"]']  # Поле "Комментарий"

    # Данные для заказа: Форма 2
    SECOND_FORM_DATA = {
        'delivery_date': [[0, 0, 0], [0, 1, 0]], # day, month, year \ 0 = now
        'rent_term': ['сутки', 'шестеро суток'],
        'scooter_color': ['black', 'grey'],
        'comment': ['коммент', 'comment']
    }

    # Модальное окно подтверждения заказа
    CONFIRM_WINDOW_TITLE = [By.XPATH, '//div[text()="Хотите оформить заказ?"]']  # Титул модального окна
    CONFIRM_WINDOW_ORDER_BUTTON = [By.XPATH, '//button[text()="Да"]']  # Кнопка "Да"

    # Модальное окно информации о заказе
    ORDER_INFO_TITLE = [By.XPATH, '//div[text()="Заказ оформлен"]']  # Титул окна информации о заказе

    def __init__(self, driver):
        self.driver = driver

    def go_order_page(self):
        self.driver.get(self.ORDER_PAGE_URL)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.FIRST_FORM_PAGE_TITLE))

    def get_first_order_page_title(self):
        return self.driver.find_element(*self.FIRST_FORM_PAGE_TITLE).text

    def enter_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def enter_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def enter_address(self, address):
        self.driver.find_element(*self.ADDRESS_FIELD).send_keys(address)

    def choose_metro_station_value_via_list(self, station_name):
        self.driver.find_element(*self.METRO_STATION_FIELD).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.METRO_STATION_LIST))
        self.driver.find_element(*self.METRO_STATION_VALUE(station_name)).click()

    def choose_metro_station_value_via_type(self, station_name):
        self.driver.find_element(*self.METRO_STATION_FIELD).send_keys(station_name)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.METRO_STATION_LIST))
        self.driver.find_element(*self.METRO_STATION_VALUE(station_name)).click()

    def enter_tel_number(self, tel_number):
        self.driver.find_element(*self.TEL_NUM_FIELD).send_keys(tel_number)

    def click_continue(self):
        self.driver.find_element(*self.FIRST_FORM_CONTINUE_BUTTON).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.SECOND_FORM_PAGE_TITLE))

    def choose_delivery_date_via_datepicker(self, day_month):
        current_day = datetime.date.today().day

        self.driver.find_element(*self.DELIVERY_DATE_FIELD).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.CURRENT_MONTH))
        for _ in range(day_month[1]):
            self.driver.find_element(*self.NEXT_MONTH_BUTTON).click()
        current_month_and_year = self.driver.find_element(*self.CURRENT_MONTH).text.replace('ь', 'я')
        day = current_day if day_month[0] == 0 else day_month[0]
        self.driver.find_element(*self.DAY(current_month_and_year=current_month_and_year, day=day)).click()

    def choose_delivery_date_via_type(self, date):
        current_day = datetime.date.today().day
        current_month = datetime.date.today().month
        current_year = datetime.date.today().year

        day = current_day if date[0] == 0 else date[0]
        month = current_month if date[1] == 0 else current_month + date[1]
        year = current_year if date[2] == 0 else date[2]
        date = f'{day}.{month}.{year}'
        self.driver.find_element(*self.DELIVERY_DATE_FIELD).send_keys(date)
        self.driver.find_element(*self.DELIVERY_DATE_FIELD).send_keys(Keys.ENTER)

    def choose_term_value(self, term_value):
        self.driver.find_element(*self.RENT_TERM_FIELD).click()
        self.driver.find_element(*self.RENT_TERM_VALUE(term_value)).click()

    def choose_scooter_color(self, color):
        self.driver.find_element(*self.SCOOTER_COLOR_VALUE(color)).click()

    def enter_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def complete_order(self):
        self.driver.find_element(*self.SECOND_FORM_COMPLETE_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.CONFIRM_WINDOW_TITLE))

    def confirm_order(self):
        self.driver.find_element(*self.CONFIRM_WINDOW_ORDER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.ORDER_INFO_TITLE))

    def get_order_info_title_text(self):
        title_text = self.driver.find_element(*self.ORDER_INFO_TITLE).text
        return title_text
