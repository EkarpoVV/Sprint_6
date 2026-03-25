
from pages.main_page import MainPage
from data import *
from pages.order_page import OrderPage
import allure

class TestOrder:
    @allure.title("Тест на проверку верхней кнопки 'Заказать'")
    def test_top_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.clicl_order_top_button()
        
        order_page = OrderPage(driver)
        order_page.set_first_name_input(DataFirstOrder.name)
        order_page.set_last_name_input(DataFirstOrder.surname)
        order_page.set_adress_input(DataFirstOrder.address)
        order_page.choice_andeground_station_input(DataFirstOrder.metro)
        order_page.set_phone_input(DataFirstOrder.phone_number)
        order_page.click_next_button()
        order_page.set_when_scooter_delivered()
        order_page.set_rent_period()
        order_page.set_scooter_colour()
        order_page.set_comment(DataFirstOrder.comment)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.confirmation_popup_check()

    @allure.title("Тест на проверку нижней кнопки 'Заказать'")
    def test_down_order_button(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_down_button()
        
        order_page = OrderPage(driver)
        order_page.set_first_name_input(DataSecondOrder.name)
        order_page.set_last_name_input(DataSecondOrder.surname)
        order_page.set_adress_input(DataSecondOrder.address)
        order_page.choice_andeground_station_input(DataSecondOrder.metro)
        order_page.set_phone_input(DataSecondOrder.phone_number)
        order_page.click_next_button()
        order_page.set_when_scooter_delivered()
        order_page.set_rent_period()
        order_page.set_scooter_colour()
        order_page.set_comment(DataSecondOrder.comment)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.confirmation_popup_check()


