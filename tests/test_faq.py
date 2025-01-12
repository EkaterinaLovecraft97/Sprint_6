import allure
import pytest
from resources.data import Data

@allure.epic("Тестирование 'Вопросы о важном'")
class TestFaq:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description('Проверяем, что по клику на стрелочку с вопросом, открывается соответсвующий ответ')
    @pytest.mark.parametrize("index, expected_answer", Data.FAQ_DATA)
    def test_faq_questions(self, main_page, index, expected_answer):
        """Тест на проверку раскрытия вопросов и правильных ответов с параметризацией."""
        main_page.scroll_to_block_faq()
        question_text = main_page.click_on_question(index)
        assert question_text, "Вопрос не был найден или некорректен."
        answer_text = main_page.get_answer(index)
        assert answer_text == expected_answer, f"Ожидался ответ '{expected_answer}', но был получен '{answer_text}'."
