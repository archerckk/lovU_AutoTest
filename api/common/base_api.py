import requests
import yaml


with open('../config/server_config.yml') as f:
    server_config=yaml.safe_load(f)


class BaseApi:

    def send(self,data:dict):
        data['url']=str(data['url']).replace('{{host}}',server_config['url'][server_config['default']])
        return requests.request(**data)

