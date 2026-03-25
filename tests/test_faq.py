from pages.main_page import MainPage
import pytest
from data import *
import allure


class TestFaq: 
    @allure.title("Тест проверки текста вопросов о важном")
    @pytest.mark.parametrize('question_text, expected_text', Data.questions )
    def test_important_questions_list(self, driver, question_text, expected_text):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.scroll_for_questions_list()
        main_page.click_important_questions_list(question_text)
        assert main_page.check_important_questions_list(expected_text)