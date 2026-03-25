from selenium.webdriver.common.by import By

class OrderPageLocators:
    FIRST_NAME = (By.XPATH, '//input[@placeholder = "* Имя"]')
    LAST_NAME = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    ADRESS = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')
    UNDEGROUN_STATION = (By.XPATH, '//input[@placeholder = "* Станция метро"]')
    PHONE = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')

    WHEN_SCOOTER_DELIVERED = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')
    WHEN_SCOOTER_DELIVERED_CALENDAR = (By.CLASS_NAME, "react-datepicker__month-container")
    WHEN_SCOOTER_DELIVERED_NEXT_MONTH_BUTTON = ('//button[text()="Next Month"]')
    WHEN_SCOOTER_DELIVERED_DATE = (By.XPATH, "//div[text()='10']")
    RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    TWO_DAYS = (By.XPATH, "//div[@class='Dropdown-option' and text()='двое суток']")
    FIRST_NAME = (By.XPATH, '//input[@placeholder = "* Имя"]')
    COLOUR_SCOOTER = (By.ID, "black")
    COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]')
    YES_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_PLACED = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')