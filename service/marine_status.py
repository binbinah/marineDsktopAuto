# -*- coding: utf-8 -*-

import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
import pyperclip
import time


class MarineStatusService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineStatusService, self).__init__()
        self.monitor_result = {}

    def read_chrome_address(self):
        """
        读取浏览器 URL 地址
        """
        with pyautogui.hold(self.locate_address_keymap[0]):
            pyautogui.press(self.locate_address_keymap[1])
        with pyautogui.hold(self.cmd):
            pyautogui.press("c")
        address = pyperclip.paste()
        return address


if __name__ == "__main__":
    time.sleep(3)
    marine_status_service = MarineStatusService()
    marine_status_service.read_chrome_address()
    print(marine_status_service.read_chrome_address())
