import allure
from data import Urls
from selenium.webdriver.common.by import By
from locators.faq_locators import FaqLocators
from .base_page import BasePage


class QestionsPage(BasePage):
    @allure.step("Открытие браузера")
    def open_browser(self):
        self.open(Urls.MAIN_PAGE_URL)
        return self

    @allure.step("Путь к вопросам")
    def scroll_to_faq(self):
        locator = (By.CLASS_NAME,"accordion")
        element = self.find_element(locator)
        self.scroll_to_element(element)
        return self

    @allure.step("Извлечение вопроса")
    def get_question(self,index):
        question_locator = (FaqLocators.QUESTION[0],FaqLocators.QUESTION[1].format(index))
        question = self.wait_for_element_to_be_clickable(question_locator)
        question.click()
        return question.text

    @allure.step("Извелечение ответа")
    def get_answers(self,index):
        answers_locator = (FaqLocators.ANSWER[0],FaqLocators.ANSWER[1].format(index))
        answers = self.find_element(answers_locator)
        return answers.text