from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePageLocators:
    login_model = (By.CLASS_NAME, "commonModal__close")
    flight_menu = (By.CLASS_NAME, "menu_Flights")
    round_trip = (By.XPATH, "//li[text()='Round Trip']")
    from_city = (By.ID, "fromCity")
    from_type_ahead = (By.XPATH, "//input[@placeholder='From']")
    from_option = (By.XPATH, "//p[text()='Rajiv Gandhi International Airport']")
    to_city = (By.ID, "toCity")
    to_type_ahead = (By.XPATH, "//input[@placeholder='To']")
    to_option = (By.XPATH, "//p[text()='Chennai International Airport']")
    departure_date_label = (By.XPATH, "//span[text()='Departure']")
    departure_date = (By.CLASS_NAME, "DayPicker-Day--today")
    return_date = (By.XPATH, "(//div[@class='dateInnerCell']/p[text()='1'])[3]")
    search_button = (By.XPATH, "//p[@data-cy='submit']")