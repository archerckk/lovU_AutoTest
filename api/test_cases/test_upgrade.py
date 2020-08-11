import allure
import pytest

from api.common.upgrade import Upgrade
import yaml

# data = {
#     "method": "post",
#     'url': "{{host}}/api/user/getUserVersionUpgrade",
#     "token": 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjI1M2VhYzQ4OTJiNTA2NjlmMDYzMjhiOTBiYjczMzU0ZjNlODcxZTQyZTY5YzllNmQwYmM5NWQ0ZTA0MjlmYjVmZjNkMTJhYjUzYTNjY2NkIn0.eyJhdWQiOiI5IiwianRpIjoiMjUzZWFjNDg5MmI1MDY2OWYwNjMyOGI5MGJiNzMzNTRmM2U4NzFlNDJlNjljOWU2ZDBiYzk1ZDRlMDQyOWZiNWZmM2QxMmFiNTNhM2NjY2QiLCJpYXQiOjE1OTcwNDY3NTYsIm5iZiI6MTU5NzA0Njc1NiwiZXhwIjoxNTk4MzQyNzU2LCJzdWIiOiI0MjMiLCJzY29wZXMiOltdfQ.b_uq7Ks5LBVkvH_456WUoFaQr305cqgffJhbeqrgCMtaLiXg_Me1yQQUDrod9xhwsczBWneIoiLsM24Qp9iMSFCOHO_hZIpEO_iVIRsGGLtH44wnycNvGbfe6uBmI1-zhrbOzV_E-Ru_g7_VHoGH3yPmimfvCVpF86qrhZc3fA1N8rs3htEWZtLi9tK7fJH_u4RCeQF9cdsQAvsfri9oKmss4c_XIcZwQijAaep-ZTgN9AnASiW56qXaWRCRC_asDBjD43Qe9uVDyzgpLvkh2zBP-JyLFsAMKx-K7GvI6QlyKE9M27hp8jSJ84i1e2hmzmfXDv4_4GaDQnKLpQwwHc6AzJw6190JOxjL_WrWRedJe6ebOSm-Fadd-9RUa5VFMhk8ptxpA-Ma4u0VatZoGrSbJtOMDAHKGB2CYUOCdKoFISKX2usUrWrhCW_uN7R5qlXv-n1aXFZtuxJsu-mS1wQAogN2GQjHjVexrTc_ZC0rPZioKtpN3I5792mtqDsM4kNdNGyHt8xofhqhjCJ-u5fhEuAAsXv1wzpyyePuS_tLmAsZShShuqO8yM_wJCKIx6Rv4Cm_nY38pQIFzbtVq7QvzhaduivYGUsKyN3WA4YhBEHXRmcoV3TQkgXaIJ1XkKfxOfJaW84_-mCcVLICjF7jDO-m7-qsjqIrgME45DU',
#     "json": {
#         "version_code": 1,
#         "lang": "en"
#     }
#
# }




class TestUpgrade:

    def setup(self):
        self.upgrage = Upgrade()

    def teardown(self):
        pass

    @allure.story('')
    @pytest.mark.parametrize('version_code,lang',[(None,''),(13,''),('','en'),(100,'')])
    def test_get_User_Version_Upgrade(self,version_code,lang):
        res = self.upgrage.get_User_Version_Upgrade(version_code, lang).json()

        if version_code is None and lang in ['en','']:
            with allure.step('测试版本传空,语言传空'):
                miss_code='The version code field is required.'
                assert res['message']==miss_code

        if version_code in [13,''] and lang in['','en']:
            with allure.step('测试版本传可升级版本,语音上传正确语言码'):
                assert res['message']=='success'
                assert res['code']==200
                assert res['data']['content'] is not None

        elif version_code == 100 and lang == '':
            with allure.step('测试版本传可升级版本,语言传空'):
                assert res['message'] == 'no update required'
                assert res['code'] == 301

