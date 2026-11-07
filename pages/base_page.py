from abc import ABC


class BasePage(ABC):

    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    @property
    def title(self):
        return self.driver.title

    @property
    def current_url(self):
        return self.driver.current_url
