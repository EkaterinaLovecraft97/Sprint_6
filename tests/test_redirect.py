import allure
from resources.test_data import Data

@allure.title('Проверка перехода на главную страницу «Самоката» по логотипу')
@allure.description('Проверяем, что при нажатии на логотип «Самоката» происходит переход на главную страницу «Самоката».')
def test_logo_scooter_redirect_to_home(order_page):
    """Тест на проверку перехода по логотипу «Самоката»."""
    order_page.click_scooter_logo()  # Нажатие на логотип «Самоката»
    assert order_page.is_home_page_opened(), "Не произошел переход на главную страницу «Самоката»"

@allure.title('Проверка открытия главной страницы Дзена по логотипу Яндекса')
@allure.description('Проверяем, что при нажатии на логотип Яндекса открывается главная страница Дзена в новом окне.')
def test_logo_yandex_redirect_to_dzen(order_page):
    """Тест на проверку перехода по логотипу Яндекса."""
    order_page.click_yandex_logo()  # Нажатие на логотип Яндекса
    order_page.switch_to_new_window()  # Переключение на новое окно
    order_page.wait_for_open_page(Data.DZEN_URL)
    assert order_page.is_dzen_page_opened(), "Не произошел переход на главную страницу Дзена"
