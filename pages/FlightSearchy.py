from locators.locatorHomePage import *
from pages.BasePage import BasePage


class FlightSearchy(BasePage):

    def __init__(self, driver):
        # Import the locators for this page.
        self.locator = HomePageLocators
        super().__init__(driver)

    def close_login_model(self):
        # Close login model
        self.find_element(self.locator.login_model).click()

    def click_flight_menu(self):
        # Click on flights menu
        self.find_element(self.locator.flight_menu).click()

    def click_round_trip(self):
        # Click on round trip
        self.find_element(self.locator.round_trip).click()

    def enter_from_city(self):
        # Enter from city
        self.find_element(self.locator.from_city).click()
        self.find_element(self.locator.from_type_ahead).send_keys("HYD")
        self.find_element(self.locator.from_option).click()

    def enter_to_city(self):
        # Enter to city
        self.find_element(self.locator.to_city).click()
        self.find_element(self.locator.to_type_ahead).send_keys("MAA")
        self.find_element(self.locator.to_option).click()
    def select_departure_date(self):
        # select departure date
        self.find_element(self.locator.departure_date_label).click()
        self.find_element(self.locator.departure_date).click()

    def select_return_date(self):
        # select return date
        self.find_element(self.locator.return_date).click()

    def click_search_button(self):
        # Click on search button
        self.find_element(self.locator.search_button).click()
