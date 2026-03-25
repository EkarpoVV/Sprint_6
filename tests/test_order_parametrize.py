
from pages.main_page import MainPage
from data import *
from pages.order_page import OrderPage
import allure
import pytest

class TestOrder1:
    @allure.title("Тест на проверку двух кнопок 'Заказать'")
    @pytest.mark.parametrize('button,name,surname,adress,metro,phone_number,comment', PersonData.person_data)
    def test_order_button_parametrize(self, driver,button,name,surname,adress,metro,phone_number,comment):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.click_order_button(button)
        
        order_page = OrderPage(driver)
        order_page.set_first_name_input(name)
        order_page.set_last_name_input(surname)
        order_page.set_adress_input(adress)
        order_page.choice_andeground_station_input(metro)
        order_page.set_phone_input(phone_number)
        order_page.click_next_button()
        order_page.set_when_scooter_delivered()
        order_page.set_rent_period()
        order_page.set_scooter_colour()
        order_page.set_comment(comment)
        order_page.click_order_button()
        order_page.click_yes_button()
        assert order_page.confirmation_popup_check()


