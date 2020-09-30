from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
from ui.pages.feature_video_waiting_page import FeatureVideoWaitingPage
from ui.pages.random_match_page import RandomMatchPage


class MainPage(BasePage):
    random_title_loc = (By.XPATH, '//*[@text="Random"]')
    invite_icon_loc = (By.XPATH, '//*[@class="android.view.ViewGroup"]//*[@class="android.widget.ImageView"][3]')

    def switch_to_random(self):
        self.steps('../pages/main_page.yml', 'switch_to_random')
        return RandomMatchPage(self._driver)


    def feature_video_invite(self):
        self.steps('../pages/main_page.yml', 'feature_video_invite')
        return FeatureVideoWaitingPage(self._driver)