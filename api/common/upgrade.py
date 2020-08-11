import yaml

from api.common.base_api import BaseApi


with open('../config/api_payload_data.yml', 'r')as f:
    data = yaml.safe_load(f)['get_User_Version_Upgrade']
    print(data)

with open('../config/server_config.yml')as f:
    token_data=yaml.safe_load(f)
    token=token_data['token'][token_data['default']]

class Upgrade(BaseApi):

    def get_User_Version_Upgrade(self,version_code,lang):
        data['json']['version_code']=version_code
        data['json']['lang']=lang
        data['headers']['Authorization']=token
        res=self.send(data)
        return res