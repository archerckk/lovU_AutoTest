from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage


class RandomVideoPage(BasePage):
    coin_confirm_loc=(By.XPATH,'//*[@text="Confirm"]')

    def wait(self):
        if self._finds(self.coin_confirm_loc):
            self._find(self.coin_confirm_loc).click()
        else:
            pass