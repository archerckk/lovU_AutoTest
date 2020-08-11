import requests
import yaml


count=0

with open('../config/server_config.yml') as f:
    server_config=yaml.safe_load(f)
    # print('服务器配置：',server_config['url'][server_config['default']])

def get_config():
    global count
    with open('../config/api_payload_data.yml', 'r')as f:
        data = yaml.safe_load(f)

    with open('../config/server_config.yml')as f:
        token_data = yaml.safe_load(f)
        token = token_data['token'][token_data['default']]
    count+=1
    print(count)
    return data,token



class BaseApi:

    def send(self,data:dict):
        data['url']=str(data['url']).replace('{{host}}',server_config['url'][server_config['default']])
        return requests.request(**data)

