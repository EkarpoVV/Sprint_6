from  selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data import Config
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Подождать видимости элемента")
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    @allure.step("Подождать и кликнуть на элемент")
    def wait_and_click(self, locator):  
        element = self.wait_and_find_element(locator)
        element.click()

    @allure.step("Подождать видимости текста")
    def wait_text_and_find_element(self, locator, text):
        WebDriverWait(self.driver, Config.DEFAULT_TIMEOUT).until(EC.text_to_be_present_in_element(locator, text))
        return self.driver.find_element(*locator)
    
    @allure.step("Ввести текст в поле ввода")
    def send_keys(self, locator, text):
        element = self.wait_and_find_element(locator)
        element.send_keys(text)

    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element) 

    @allure.step("Переключить браузер на последню вкладку")
    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.wait_for_page_load()

    @allure.step("Ждем загрузки страницы")
    def wait_for_page_load(self, timeout=20):
        WebDriverWait(self.driver, timeout).until(
        lambda d: d.execute_script("return document.readyState") == "complete"
        )

    @allure.step("Получить URL страницы")
    def get_current_url(self):
        return self.driver.current_url