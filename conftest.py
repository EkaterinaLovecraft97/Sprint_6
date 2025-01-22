import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

from pages.main_page import MainPage
from pages.order_page import OrderPage
from resources.data import Data

@pytest.fixture
def order_page(driver):
    driver.get(Data.ORDER_PAGE_URL)
    return OrderPage(driver)

@pytest.fixture
def main_page(driver):
    driver.get(Data.MAIN_PAGE_URL)
    return MainPage(driver)

@pytest.fixture
def driver():
    service = Service()

    # Укажите путь к исполняемому файлу Firefox
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"

    # Инициализация Firefox WebDriver
    driver = webdriver.Firefox(service=service, options=options)

    # Возвращаем WebDriver для использования в тестах
    yield driver

    # Закрываем браузер после завершения теста
    driver.quit()

