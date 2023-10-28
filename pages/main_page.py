from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage


class MainPage():

    MAIN_PAGE_LINK = 'https://qa-scooter.praktikum-services.ru/'  # Ссылка на главную страницу
    IMPORTANT_QUESTIONS_TITLE = [By.XPATH, "//div[text()='Вопросы о важном']"]  # Заголовок блока "Вопросы о важном"
    IMPORTANT_QUESTUION = lambda self, question_num: [By.XPATH, f"//div[@data-accordion-component='Accordion']/div[{question_num}]"]  # Влажный вопрос
    OPENED_ANSWER = [By.XPATH, '//div[@aria-expanded="true"]/parent::div/following-sibling::div/p']  # Открытый вопрос
    SCOOTER_PIC = [By.XPATH, '//img[@src="/assets/scooter.png"]']  # Картинка самоката на главной
    COOKIE_CONFIRM_BUTTON = [By.XPATH, '//button[@id="rcc-confirm-button"]']  # Кнопка согласия на куки
    GET_ORDER_HEADER_BUTTON = [By.XPATH, '//div[starts-with(@class, "Header_Nav")]/button[text()="Заказать"]']  # Кнопка "Заказать" в хереде
    GET_ORDER_BODY_BUTTON = [By.XPATH, '//div[starts-with(@class, "Home_RoadMap")]//button[text()="Заказать"]']  # Кнопка "Заказать" в теле

    def __init__(self, driver):
        self.driver = driver

    def go_main_page_by_link(self):
        self.driver.get(self.MAIN_PAGE_LINK)
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(self.SCOOTER_PIC))

    def get_link(self):
        return self.driver.current_url

    def confirm_cookie(self):
        self.driver.find_element(*self.COOKIE_CONFIRM_BUTTON).click()

    def scroll_to_important_questions(self):
        list_title = self.driver.find_element(*self.IMPORTANT_QUESTIONS_TITLE)
        self.driver.execute_script("arguments[0].scrollIntoView();", list_title)
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.IMPORTANT_QUESTIONS_TITLE))

    def open_answer(self, question_num):
        self.driver.find_element(*self.IMPORTANT_QUESTUION(question_num)).click()
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.OPENED_ANSWER))

    def get_opened_answer_text(self, question_num):

        return self.driver.find_element(*self.OPENED_ANSWER).text

    def click_order_header_button(self):
        self.driver.find_element(*self.GET_ORDER_HEADER_BUTTON).click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(OrderPage.FIRST_FORM_PAGE_TITLE))

    def click_order_body_button(self):
        body_order_button_elem = self.driver.find_element(*self.GET_ORDER_HEADER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", body_order_button_elem)
        body_order_button_elem.click()
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located(OrderPage.FIRST_FORM_PAGE_TITLE))
