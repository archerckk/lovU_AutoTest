import allure
import pytest

from api.common.upgrade import Upgrade



class TestUpgrade:

    def setup(self):
        self.upgrage = Upgrade()

    def teardown(self):
        pass

    # @allure.story('')
    @pytest.mark.parametrize('version_code,lang',[(None,''),(13,''),('','en'),(100,'')])
    def test_get_User_Version_Upgrade(self,version_code,lang):
        res = self.upgrage.get_User_Version_Upgrade(version_code, lang).json()

        if  res['code']==202:
            raise Exception('后台没有配置最新版本信息')

        if version_code in [13,''] and lang in['','en']:
            with allure.step('验证正常提示升级'):
                assert res['message']=='success'
                assert res['code']==200
                assert res['data']['content'] is not None

        elif version_code == 100 and lang == '':
            with allure.step('验证升级不'):
                assert res['message'] == 'no update required'
                assert res['code'] == 301

