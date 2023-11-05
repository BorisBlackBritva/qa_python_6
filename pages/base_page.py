from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def get_link(self):
        return self.driver.current_url

    def get(self, link):
        self.driver.get(link)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.driver.find_element(*locator).click()

    def get_elem_text(self, locator):
        return self.driver.find_element(*locator).text

    def wait(self, condition, locator):
        return WebDriverWait(self.driver, 7).until(condition(locator))

    def scroll(self, elem):
        self.driver.execute_script("arguments[0].scrollIntoView();", elem)

    def send_keys(self, locator, key):
        self.find_element(locator).send_keys(key)

    def switch_page(self, num):
        tab_handles = self.driver.window_handles
        self.driver.switch_to.window(tab_handles[num])
