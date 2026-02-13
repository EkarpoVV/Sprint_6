from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure



class MainPage(BasePage):

    @allure.step("Кликнуть на кнопку 'Принять куки'")
    def accept_cookies(self):
        self.wait_and_click(MainPageLocators.COOCKIE_ACCEPT)
    
    @allure.step("Проскролить страницу до FAQ")
    def scroll_for_questions_list(self):
        self.scroll_to_element(MainPageLocators.FAQ_LIST)

    @allure.step("Кликнуть на стрелку каждого FAQ'")
    def click_important_questions_list(self, question_text):
        self.wait_and_click(MainPageLocators.question_text(question_text))

    @allure.step("Проверяем текст вопроса и текст ответа в FAQ")
    def check_important_questions_list(self, expected_text):
        element = self.wait_and_find_element(MainPageLocators.ansver_text(expected_text))
        return element.text == expected_text
    
    @allure.step("Кликнуть на кнопку 'Заказать' в хедере")
    def clicl_order_top_button(self):
        self.wait_and_click(MainPageLocators.ORDER_TOP_BUTTON)

    @allure.step("Кликнуть на кнопку 'Заказать' в середине страницы")
    def click_order_down_button(self):
        self.wait_and_click(MainPageLocators.ORDER_DOWN_BUTTON)

    @allure.step("Кликнуть на логотип 'Яндекс' в хедере")
    def click_logo_yandex(self):
        self.wait_and_click(MainPageLocators.LOGO_YANDEX)

    @allure.step("Кликнуть на логотип 'Самоката' в хедере")
    def click_logo_scooter(self):
        self.wait_and_click(MainPageLocators.LOGO_SCOOTER)

    @allure.step("Кликнуть на кнопку 'Заказать'")
    def click_order_button(self,button):
        self.wait_and_click(button)

