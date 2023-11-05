from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.order_page import OrderPage
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    MAIN_PAGE_LINK = 'https://qa-scooter.praktikum-services.ru/'  # Ссылка на главную страницу
    IMPORTANT_QUESTIONS_TITLE = [By.XPATH, "//div[text()='Вопросы о важном']"]  # Заголовок блока "Вопросы о важном"
    IMPORTANT_QUESTUION = lambda self, question_num: [By.XPATH, f"//div[@data-accordion-component='Accordion']/div[{question_num}]"]  # Влажный вопрос
    OPENED_ANSWER = [By.XPATH, '//div[@aria-expanded="true"]/parent::div/following-sibling::div/p']  # Открытый вопрос
    SCOOTER_PIC = [By.XPATH, '//img[@src="/assets/scooter.png"]']  # Картинка самоката на главной
    COOKIE_CONFIRM_BUTTON = [By.XPATH, '//button[@id="rcc-confirm-button"]']  # Кнопка согласия на куки
    GET_ORDER_HEADER_BUTTON = [By.XPATH, '//div[starts-with(@class, "Header_Nav")]/button[text()="Заказать"]']  # Кнопка "Заказать" в хереде
    GET_ORDER_BODY_BUTTON = [By.XPATH, '//div[starts-with(@class, "Home_RoadMap")]//button[text()="Заказать"]']  # Кнопка "Заказать" в теле

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переходим на главную страницу')
    def go_main_page_by_link(self):
        self.get(self.MAIN_PAGE_LINK)
        self.wait(EC.presence_of_element_located, self.SCOOTER_PIC)

    @allure.step('Подтверждаем куки')
    def confirm_cookie(self):
        self.click(self.COOKIE_CONFIRM_BUTTON)
        self.wait(EC.invisibility_of_element_located, self.COOKIE_CONFIRM_BUTTON)

    @allure.step('Скролл к влажным вопросам')
    def scroll_to_important_questions(self):
        list_title = self.find_element(self.IMPORTANT_QUESTIONS_TITLE)
        self.scroll(list_title)
        self.wait(EC.visibility_of_element_located, self.IMPORTANT_QUESTIONS_TITLE)

    @allure.step('Открываем ответ на влажный вопрос')
    def open_answer(self, question_num):
        self.wait(EC.visibility_of_element_located, self.IMPORTANT_QUESTUION(question_num))
        self.click(self.IMPORTANT_QUESTUION(question_num))
        self.wait(EC.visibility_of_element_located, self.OPENED_ANSWER)

    @allure.step('Получаем текст открытого ответа')
    def get_opened_answer_text(self):
        return self.get_elem_text(self.OPENED_ANSWER)

    @allure.step('Нажимаем кнопку "Заказать" на главной странице в шапке')
    def click_order_header_button(self):
        self.click(self.GET_ORDER_HEADER_BUTTON)
        self.wait(EC.presence_of_element_located, OrderPage.FIRST_FORM_PAGE_TITLE)

    @allure.step('Нажимаем кнопку "Заказать" на главной странице в теле')
    def click_order_body_button(self):
        body_order_button_elem = self.find_element(self.GET_ORDER_HEADER_BUTTON)
        self.scroll(body_order_button_elem)
        body_order_button_elem.click()
        self.wait(EC.presence_of_element_located, OrderPage.FIRST_FORM_PAGE_TITLE)
