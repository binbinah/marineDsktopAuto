# -*- coding: utf-8 -*-

import pyautogui
import pyperclip
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from service.marine_status import MarineStatusService
from typing import Dict
import time


class MarineLoginService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self,host):
        super(MarineLoginService, self).__init__()
        self.host = host

    def login_main(self):

        with pyautogui.hold(self.locate_address_keymap[0]):
            pyautogui.press(self.locate_address_keymap[1])
        pyperclip.copy(self.config["cnc_signin_url"].format(host=self.host))
        with pyautogui.hold(self.cmd):
            pyautogui.press("v")
        pyautogui.press("enter", presses=2, interval=1)
        time.sleep(5)
        try:
            self.login_fill()
        except TypeError as e:
            marine_status_service = MarineStatusService()
            address = marine_status_service.read_chrome_address()
            if self.config["cnc_line_url"].format(host=self.host) == address:
                with pyautogui.hold(self.locate_address_keymap[0]):
                    pyautogui.press(self.locate_address_keymap[1])
                # pyautogui.write(self.config["quoting_url"], interval=0.1)
                pyperclip.copy(self.config["quoting_url"].format(host=self.host))
                with pyautogui.hold(self.cmd):
                    pyautogui.press("v")
                pyautogui.press("enter", presses=2, interval=0.1)
                time.sleep(2)

        time.sleep(5)

    def login_button_click(self) -> Dict:
        """
        点击首页的登录按钮
        :return: dict(kwargs, status=status, info=info)
        """
        return self._locate_and_click(f"{self.path}/staticfile/login_button.png")

    def login_fill(self):
        with pyautogui.hold(self.cmd):
            pyautogui.press("f")
        pyperclip.copy("(Email)")
        with pyautogui.hold(self.cmd):
            pyautogui.press("v")
        pyautogui.press("enter", interval=0.1)
        pyautogui.press("esc", interval=0.1)
        pyautogui.press("tab", presses=1, interval=1)

        pyperclip.copy(self.config["username"])
        with pyautogui.hold(self.cmd):
            pyautogui.press("v")
        time.sleep(1)
        pyautogui.press("tab", interval=0.5)
        # pyautogui.write(self.config["passwd"], interval=0.1)
        pyperclip.copy(self.config["passwd"])
        with pyautogui.hold(self.cmd):
            pyautogui.press("v")
        pyautogui.press("enter")

    @staticmethod
    def _locate_and_click(path: str, clicks: int = 2):
        """
        通用的点击方法。

        :param path: 图片定位路径
        :param clicks: 点击次数
        :return:
        """
        try:
            pyautogui.click(path, clicks=clicks)
            return func_resp_wrapper(info=f'{path.split("/")[-1]}, 点击成功。')
        except TypeError:
            return func_resp_wrapper(
                status=False, info=f"没有找到{path.split('/')[-1]}，需要确认页面是否存在该图片锚点。"
            )


if __name__ == "__main__":
    service = MarineLoginService()
    service.login_main()
