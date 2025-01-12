import allure
import pytest
from resources.data import Data

@allure.epic("Тестирование страницы заказов")
class TestOrderPage:

    @allure.title('Проверка позитивного сценария заказа самоката')
    @allure.description('Проверяем весь флоу позитивного сценария с двумя наборами данных')
    @pytest.mark.parametrize("order_button, personal_info, order_details", Data.ORDER_DATA)
    def test_order_success(self, main_page, order_page, order_button, personal_info, order_details):
        """Параметризованный тест успешного оформления заказа через верхнюю и нижнюю кнопки 'Заказать'."""
        if order_button == "top":
            main_page.click_order_button_top()
        elif order_button == "bottom":
            main_page.click_order_button_bottom()

        order_page.enter_personal_info(**personal_info)
        order_page.enter_order_details(**order_details)
        assert order_page.is_order_confirmation_visible(), "Модальное окно подтверждения заказа не появилось"
