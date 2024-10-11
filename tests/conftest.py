import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service


@pytest.fixture(scope="class")
def driver_init(request):
    driver = webdriver.Edge(service=Service(executable_path='../msedgedriver.exe'))
    # driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.makemytrip.com/")
    request.cls.driver = driver

    yield

    driver.close()
