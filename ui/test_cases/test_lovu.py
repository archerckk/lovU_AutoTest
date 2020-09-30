from time import sleep
import pytest
import yaml
import random
from ui.pages.app import App

# with open('../datas/datas.yml', encoding='UTF-8')as f:
#     datas = yaml.safe_load(f)


class TestLiki:

    def setup_class(self):
        self.app = App()
        # self.main = self.app.start().main()


    def teardown_class(self):
        self.app.close()

    def test_demo(self):
        '持续点击随机匹配视频'
        random_page=self.app.start().main().switch_to_random()
        while 1:
            random_page.start_match().wait()
            sleep(2)
            self.app.back()

    def test_video_settle(self):
        feature_video_inner_page=self.app.start().main().feature_video_invite().wait_finish()
        room_id=feature_video_inner_page.send_gift()
        feature_video_inner_page.end_video()
        print(room_id)