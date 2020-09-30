from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.feature_video_inner_page import FeatureVideoInnerPage


class FeatureVideoWaitingPage(BasePage):
    cancel_icon_loc=(By.XPATH,'//*[@text="Cancel"]')

    def wait_finish(self):
         self._wait_disappear(self.cancel_icon_loc)
         return FeatureVideoInnerPage(self._driver)