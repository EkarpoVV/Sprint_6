from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
import allure

class OrderPage(BasePage):

    @allure.step("Заполнить поле 'Имя'")
    def set_first_name_input(self, first_name):
        self.send_keys(OrderPageLocators.FIRST_NAME, first_name)
    
    @allure.step("Заполнить поле 'Фамилия'")
    def set_last_name_input(self, last_name):
        self.send_keys(OrderPageLocators.LAST_NAME, last_name)
    
    @allure.step("Заполнить поле 'Адрес'")
    def set_adress_input(self, adress):
        self.send_keys(OrderPageLocators.ADRESS, adress)
    
    @allure.step("Заполнить поле 'Метро'")
    def choice_andeground_station_input(self, station):
        self.send_keys(OrderPageLocators.ADRESS, station)
        element = self.wait_and_find_element(OrderPageLocators.UNDEGROUN_STATION)
        element.send_keys(Keys.ARROW_DOWN)
        element.send_keys(Keys.ENTER)
    
    @allure.step("Заполнить поле 'Телефон'")
    def set_phone_input(self, phone):
        self.send_keys(OrderPageLocators.PHONE, phone)
    
    @allure.step("Клик на кнопку 'Далее'")
    def click_next_button(self):
        self.wait_and_click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить поле 'Когда привезти самокат'")
    def set_when_scooter_delivered(self):
        self.wait_and_click(OrderPageLocators.WHEN_SCOOTER_DELIVERED)
        self.wait_and_find_element(OrderPageLocators.WHEN_SCOOTER_DELIVERED_CALENDAR)
        #self.wait_and_click(OrderPageLocators.WHEN_SCOOTER_DELIVERED_NEXT_MONTH_BUTTON)
        #self.wait_and_find_element(OrderPageLocators.WHEN_SCOOTER_DELIVERED_CALENDAR)
        self.wait_and_click(OrderPageLocators.WHEN_SCOOTER_DELIVERED_DATE)

    @allure.step("Заполнить поле 'Период аренды'")
    def set_rent_period(self):
        self.wait_and_click(OrderPageLocators.RENTAL_PERIOD)
        self.wait_and_click(OrderPageLocators.TWO_DAYS)

    @allure.step("Заполнить поле 'Цвет'")
    def set_scooter_colour(self):
        self.wait_and_click(OrderPageLocators.COLOUR_SCOOTER)

    @allure.step("Заполнить поле 'Комментарий'")
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FOR_COURIER, comment)

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_button(self):
        self.wait_and_click(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Нажать на кнопку 'Да'")
    def click_yes_button(self):
        self.wait_and_click(OrderPageLocators.YES_BUTTON)
    
    @allure.step("Найти пупап 'Заказ оформлен'")
    def confirmation_popup_check(self):
        try:
            self.wait_and_find_element(OrderPageLocators.ORDER_PLACED)
            return True
        except:
            return False

