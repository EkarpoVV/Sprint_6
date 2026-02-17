from pages.main_page import MainPage
from pages.base_page import BasePage
from data import *
import allure
import time


class TestLogo:
    @allure.title("Тест проверки логтипа Yandex")
    def test_click_yandex_logo(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        time.sleep(4)
        main_page.click_logo_yandex()
        main_page.switch_to_last_window()
        base_page = BasePage(driver)
        current_url = base_page.get_current_url()
        assert Config.DZEN_PAGE_URL in current_url

    @allure.title("Тест проверки логотипа Самокат")
    def test_click_scooter_logo(self, driver):
        main_page = MainPage(driver)
        main_page.accept_cookies()
        main_page.clicl_order_top_button()
        main_page.click_logo_scooter()
        current_url = main_page.get_current_url()
        assert Urls.BASE_URL == current_url
