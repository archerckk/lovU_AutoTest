import yaml

from api.common.base_api import BaseApi


with open('../config/api_payload_data.yml', 'r')as f:
    data = yaml.safe_load(f)['get_User_Version_Upgrade']
    print(data)

class Upgrade(BaseApi):

    def get_User_Version_Upgrade(self,version_code,lang):
        data['json']['version_code']=version_code
        data['json']['lang']=lang
        res=self.send(data)
        return res