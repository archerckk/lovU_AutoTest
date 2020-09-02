from api.common.base_api import BaseApi,get_config


data,token=get_config()

class Upgrade(BaseApi):

    def get_user_version_upgrade(self,version_code,lang):
        api_data=data['get_user_version_upgrade']
        api_data['json']['version_code']=version_code
        api_data['json']['lang']=lang
        api_data['headers']['Authorization']=token
        res=self.send(api_data)
        return res