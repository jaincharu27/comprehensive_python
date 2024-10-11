from locators.locatorSearchPage import SearchPageLocators
from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        # Import the locators for this page.
        self.locator = SearchPageLocators

    def verify_search_page(self):
        # Close updated price pop up box
        self.find_element(self.locator.update_price_model).click()
        # Verify label for flight search from HYD to Chennai
        title = self.locator.search_page_label.text
        print(title)
        if title == "Flights from Hyderabad to Chennai, and back":
            self.assertTrue(True)
        else:
            print("Search page is not found")
            self.assertFalse(False)
