from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPage(BasePage):
    CARDS = (By.XPATH, ".//div[@class='category-cards']/a")

    def get_cards_number_on_page(self):
        cards = self.driver.find_elements(*MainPage.CARDS)
        return len(cards)
