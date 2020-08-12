from time import sleep

from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.pages.random_video_page import RandomVideoPage


class RandomMatchPage(BasePage):
    start_match_loc=(By.XPATH,'//*[@text="Start"]')

    def start_match(self):
        # sleep(2)
        self._find_focus(self.start_match_loc).click()
        return RandomVideoPage(self._driver)

