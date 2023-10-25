from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    SCOOTER_LOGO = [By.XPATH, '//img[@src="/assets/scooter.svg"]']