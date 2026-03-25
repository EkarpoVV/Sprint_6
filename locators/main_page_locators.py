from selenium.webdriver.common.by import By

class MainPageLocators:
    COOCKIE_ACCEPT = (By.ID, 'rcc-confirm-button')
    FAQ_LIST = (By.CLASS_NAME, "accordion__button")
    ORDER_TOP_BUTTON = (By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]')
    ORDER_DOWN_BUTTON = (By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]')
    LOGO_YANDEX = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']/img[@alt='Yandex']")
    LOGO_SCOOTER = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]/img[@alt="Scooter"]')

    @staticmethod
    def question_text(question_text):
        return By.XPATH, f'//div[text()="{question_text}"]'
    
    @staticmethod
    def ansver_text(expected_text):
        return By.XPATH, f"//p[text()='{expected_text}']"
    
