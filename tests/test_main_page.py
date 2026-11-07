import data
from pages.main_page import MainPage


class TestMainPage:

    def test_main_page_is_available(self, driver):
        main_page = MainPage(driver)
        main_page.open(data.BASE_URL)

        assert main_page.title == data.DEMOQA_TITLE_ON_MAIN_PAGE
