import allure
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from resources.data import Data

class OrderPage(BasePage):
    # Локаторы для формы заказа
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_STATION_LIST = (By.CLASS_NAME, "select-search__row")  # Для выбора станции из списка
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Локаторы для второй части формы (даты и времени)
    DELIVERY_DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-placeholder")  # Для выбора периода аренды
    RENTAL_PERIOD_OPTION = "//div[contains(@class, 'Dropdown-option') and text()='{}']"  # Подставить период
    ORDER_COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and @class='Button_Button__ra12g Button_Middle__1CSJM']")
    CONFIRM_ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")

    # Локаторы для проверки успешного заказа
    ORDER_CONFIRMATION_MODAL = (By.CLASS_NAME, "Order_Modal__YZ-d3")

    SCOOTER_LOGO = (By.XPATH, ".//a[@href='/']")
    YANDEX_LOGO = (By.XPATH, ".//a[@href='//yandex.ru']")

    # Методы
    @allure.step("Метод ввода персональных данных")
    def enter_personal_info(self, name: str, surname: str, address: str, metro_station: str, phone: str):
        """Вводим личные данные."""
        self._enter_text(self.NAME_INPUT, name)
        self._enter_text(self.SURNAME_INPUT, surname)
        self._enter_text(self.ADDRESS_INPUT, address)
        self._enter_text(self.METRO_STATION_INPUT, metro_station)
        self._select_first_metro_station()
        self._enter_text(self.PHONE_INPUT, phone)
        self._click(self.NEXT_BUTTON)

    @allure.step("Метод ввода деталей заказа")
    def enter_order_details(self, delivery_date: str, rental_period: str, color: str, comment: str):
        """Вводим детали заказа."""
        self._click(self.RENTAL_PERIOD_DROPDOWN)
        self._select_rental_period(rental_period)
        self._select_scooter_color(color)
        self._enter_text(self.ORDER_COMMENT_INPUT, comment)
        self._enter_text(self.DELIVERY_DATE_INPUT, delivery_date)
        self._click(self.ORDER_BUTTON)
        self._click(self.CONFIRM_ORDER_BUTTON)

    @allure.step("Метод проверки видимости модального окна")
    def is_order_confirmation_visible(self) -> bool:
        """Проверяем, что модальное окно подтверждения заказа появилось."""
        return self._is_element_visible(self.ORDER_CONFIRMATION_MODAL)

    @allure.step("Вспомогательный метод ввода текста в поле")
    # Вспомогательные методы
    def _enter_text(self, locator, text: str):
        """Ввод текста в поле."""
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Вспомогательный метод клика по элементу на странице")
    def _click(self, locator):
        """Клик по элементу."""
        self.find_element(*locator).click()

    @allure.step("вспомогательный метод выбора первой станции метро из выпадающего списка")
    def _select_first_metro_station(self):
        """Выбор первой станции метро из выпадающего списка."""
        self.find_elements(*self.METRO_STATION_LIST)[0].click()

    @allure.step("Вспомогательный метод выбора срока аренды")
    def _select_rental_period(self, rental_period: str):
        """Выбор периода аренды."""
        option_locator = (By.XPATH, self.RENTAL_PERIOD_OPTION.format(rental_period))
        self.find_element(*option_locator).click()

    @allure.step("Вспомогательный метод выбора цвета самоката")
    def _select_scooter_color(self, color: str):
        """Выбор цвета самоката."""
        color_checkbox = (By.ID, color)
        self.find_element(*color_checkbox).click()

    @allure.step("Вспомогательный метод проверки видимости элемента страницы")
    def _is_element_visible(self, locator) -> bool:
        """Проверяет, виден ли элемент на странице."""
        try:
            self.find_element(*locator)
            return True
        except NoSuchElementException:
            return False

    @allure.step("Нажимаем на логотип «Самоката»")
    def click_scooter_logo(self):
        """Кликаем на логотип «Самоката»."""
        self.find_element(*self.SCOOTER_LOGO).click()

    @allure.step("Проверяем, открыта ли главная страница «Самоката»")
    def is_home_page_opened(self):
        """Проверяем, открыта ли главная страница «Самоката»."""
        return Data.MAIN_PAGE_URL == self.driver.current_url

    @allure.step("Нажимаем на логотип Яндекса")
    def click_yandex_logo(self):
        """Кликаем на логотип Яндекса."""
        self.find_element(*self.YANDEX_LOGO).click()

    @allure.step("Переключаемся на новое окно браузера")
    def switch_to_new_window(self):
        """Переключаемся на новое окно."""
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверяем, открыта ли главная страница Дзена")
    def is_dzen_page_opened(self):
        """Проверяем, открыта ли главная страница Дзена."""
        return Data.DZEN_URL == self.driver.current_url

    def wait_for_open_page(self, page_url):
        return WebDriverWait(self.driver, 10).until(
            EC.url_to_be(page_url))
