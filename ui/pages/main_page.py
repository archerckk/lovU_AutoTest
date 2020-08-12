from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.random_match_page import RandomMatchPage


class MainPage(BasePage):
    random_title_loc=(By.XPATH,'//*[@text="Random"]')

    def switch_to_random(self):
        self._find_focus(self.random_title_loc).click()
        return RandomMatchPage(self._driver)