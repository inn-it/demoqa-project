from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class TextBoxPage(BasePage):
    TITLE_H1 = (By.XPATH, ".//h1")
