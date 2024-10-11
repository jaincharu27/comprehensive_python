import pytest
from pages.FlightSearchy import FlightSearchy
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("driver_init")
class TestFlightSearch:

    def test_flightSearch(self):
        flight_searchy = FlightSearchy(self.driver)
        search_page = SearchPage(self.driver)

        # Close login model
        flight_searchy.close_login_model()
        # Click on Flight button to search flights
        flight_searchy.click_flight_menu()
        # Click on round trip button
        flight_searchy.click_round_trip()
        # Select from city Hyderabad
        flight_searchy.enter_from_city()
        # Select return city Chennai
        flight_searchy.enter_to_city()
        # Select Departure date
        flight_searchy.select_departure_date()
        # Select Return date
        flight_searchy.select_return_date()
        # Click on search button
        flight_searchy.click_search_button()
        # Verify search result page
        search_page.verify_search_page()


if __name__ == "__main__":
    pytest.main(["test_flightSearch.py"])



