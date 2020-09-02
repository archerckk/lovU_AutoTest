from api.common.base_api import BaseApi,get_config


data,token=get_config()

class VideoCard(BaseApi):

    def get_video_card(self,card_type):
        api_data = data['get_video_card']
        api_data['json']['card_type'] = card_type
        api_data['headers']['Authorization'] = token
        res = self.send(api_data)
        return res