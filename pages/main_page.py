import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    # Локаторы
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CLASS_NAME, "Button_Button__ra12g.Button_Middle__1CSJM")
    FAQ_LIST = (By.CLASS_NAME, "accordion")
    FAQ_QUESTION = (By.XPATH, "(.//div[@class='accordion__button'])[{}]")
    FAQ_ANSWER = (By.XPATH, "(.//div[@class='accordion__panel'])[{}]")


    @allure.step("Метод прокрутки страницы до блока FAQ")
    def scroll_to_block_faq(self):
        """Прокрутить страницу до блока FAQ."""
        self.scroll_to_element(self.FAQ_LIST)
        self.wait_for_load_element(self.FAQ_LIST)

    @allure.step("Метод клика на вопрос по индексу")
    def click_on_question(self, index):
        """Кликнуть на вопрос по индексу."""
        method, locator = self.FAQ_QUESTION
        formatted_locator = (method, locator.format(index))
        self.wait_for_load_element(formatted_locator)
        # Разделяем кортеж и передаём отдельные аргументы
        question = self.find_element(*formatted_locator)
        question.click()
        return question.text

    @allure.step("Метод получения текста ответа по индексу")
    def get_answer(self, index):
        """Получить текст ответа по индексу."""
        method, locator = self.FAQ_ANSWER
        formatted_locator = (method, locator.format(index))
        self.wait_for_load_element(formatted_locator)
        # Распаковываем кортеж в метод find_element
        return self.find_element(*formatted_locator).text

    @allure.step("Метод нажатия на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.find_element(*self.ORDER_BUTTON_TOP).click()

    @allure.step("Метод нажатия на нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        self.find_element(*self.ORDER_BUTTON_BOTTOM).click()
