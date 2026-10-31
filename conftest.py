import pytest
from selenium import webdriver


@pytest.fixture(scope="fuction")
def driver():
    driver = webdriver.CHrome()
    yield driver
    driver.quit()
