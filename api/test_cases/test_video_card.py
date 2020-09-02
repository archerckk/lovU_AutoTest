import allure
import pytest

from api.common.video_card import VideoCard


@allure.feature('用户升级提醒接口')
class TestVideoCard:

    def setup(self):
        self.video_card = VideoCard()

    def teardown(self):
        pass

    @allure.story('视频卡领取接口测试')
    def test_get_video_card(self):
        res = self.video_card.get_video_card(1).json()
        print(res)

        # if  res['code']==202:
        #     raise Exception('后台没有配置最新版本信息')
        #
        # if version_code in [13,''] and lang in['','en']:
        #     with allure.step('验证正常提示升级'):
        #         assert res['message']=='success'
        #         assert res['code']==200
        #         assert res['data']['content'] is not None
        #
        # elif version_code == 100 and lang == '':
        #     with allure.step('验证升级不'):
        #         assert res['message'] == 'no update required'
        #         assert res['code'] == 301

