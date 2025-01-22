from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, by: By, value: str):
        return self.driver.find_element(by, value)

    def find_elements(self, by: By, value: str):
        return self.driver.find_elements(by, value)

    def open_url(self, url: str):
        self.driver.get(url)

    def scroll_to_element(self, locator):
        """Прокрутить страницу до элемента."""
        by, value = locator  # Разбиваем кортеж на отдельные аргументы
        element = self.find_element(by, value)  # Передаём отдельно `by` и `value`
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def wait_for_load_element(self, locator, timeout=10):
        """Ожидание видимости элемента."""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
