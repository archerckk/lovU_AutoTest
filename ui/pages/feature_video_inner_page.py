from selenium.webdriver.common.by import By
from ui.pages.base_page import BasePage
import time
import re
import subprocess

class FeatureVideoInnerPage(BasePage):

    def send_gift(self):
        package_list=['com.social.nene']
        cmd=f'adb shell logcat |findstr {package_list[0]}'
        fhandle=open('tmp_log.txt','w')
        log=subprocess.Popen(cmd,shell=True,stdout=fhandle).stdout
        fhandle.close()

        with open('../pages/tmp_log.txt')as f:
            tmp_log_content=f.read()
        room_id_reg=re.compile(r'nene.+423_424?')
        room_id=room_id_reg.findall(tmp_log_content)[0]



        for i in range(5):
            self.steps('../pages/feature_video_inner_page.yml','send_gift')
            time.sleep(5)

        return room_id

    def end_video(self):
        self._driver.back(2)
        self.steps('../pages/feature_video_inner_page.yml','end_video')