from selenium import webdriver
from pages.main_page import MainPage
import allure

class TestImportantQuestions:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_text_answer_1_check(self):
        main_page = MainPage(self.driver)

        main_page.go_main_page_by_link()
        main_page.confirm_cookie()
        main_page.scroll_to_important_questions()
        main_page.open_answer(1)
        answer_text = main_page.get_opened_answer_text(1)

        assert answer_text == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    def test_text_answer_2_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(2)
        answer_text = main_page.get_opened_answer_text(2)

        assert answer_text == ("Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, "
                               "можете просто сделать несколько заказов — один за другим.")

    def test_text_answer_3_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(3)
        answer_text = main_page.get_opened_answer_text(3)

        assert answer_text == ("Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. "
                               "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. "
                               "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.")

    def test_text_answer_4_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(4)
        answer_text = main_page.get_opened_answer_text(4)

        assert answer_text == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    def test_text_answer_5_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(5)
        answer_text = main_page.get_opened_answer_text(5)

        assert answer_text == ("Пока что нет! Но если что-то срочное — "
                               "всегда можно позвонить в поддержку по красивому номеру 1010.")

    def test_text_answer_6_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(6)
        answer_text = main_page.get_opened_answer_text(6)

        assert answer_text == ("Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — "
                               "даже если будете кататься без передышек и во сне. Зарядка не понадобится.")

    def test_text_answer_7_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(7)
        answer_text = main_page.get_opened_answer_text(7)

        assert answer_text == ("Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. "
                               "Все же свои.")

    def test_text_answer_8_check(self):
        main_page = MainPage(self.driver)

        main_page.open_answer(8)
        answer_text = main_page.get_opened_answer_text(8)

        assert answer_text == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()