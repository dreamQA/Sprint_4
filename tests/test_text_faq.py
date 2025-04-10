import allure
import pytest
from pages.faq_page import QestionsPage
from data import QuestionsAndAnswers

class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе Вопросы о важном')
    @allure.description('Проверяем,что по клику на стрелочку с вопросом,открывается соответсвующий ответ')
    @pytest.mark.parametrize('index,question,answer', QuestionsAndAnswers.QUESTIONS_AND_ANSWERS_LIST)

    def test_check_question_and_answer(self, faq_page, index, question, answer):
        faq_page.open_browser()
        faq_page.scroll_to_faq()
        question_text = faq_page.get_question(index)
        answer_text = faq_page.get_answers(index)
        assert question_text == question
        assert answer_text == answer