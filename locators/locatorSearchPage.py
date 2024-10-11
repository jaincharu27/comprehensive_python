from selenium.webdriver.common.by import By


class SearchPageLocators:
    update_price_model = (By.XPATH, "//button[text()='OKAY, GOT IT!']")
    search_page_label = (By.XPATH, "//div[@class='listingRhs']")
