import time

import data
from pages.text_box_page import TextBoxPage


class TestTextBoxPage:

    def test_text_box_page_has_expected_url(self, driver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open(data.TEXT_BOX)

        assert text_box_page.current_url == data.TEXT_BOX

    def test_text_box_page_expected_title_h1(self, driver):
        text_box_page = TextBoxPage(driver)
        text_box_page.open(data.TEXT_BOX)

        time.sleep(2)
        assert (
            text_box_page.get_text(TextBoxPage.TITLE_H1)
            == data.TITLE_H1_TEXT_BOX
        )
        