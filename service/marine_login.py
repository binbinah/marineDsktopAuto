import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from rich import print
from typing import Dict
import time


class MarineLoginService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineLoginService, self).__init__()

    def login_main(self):

        self.login_button_click()
        time.sleep(5)
        try:
            self.login_fill()
        except TypeError as e:
            with pyautogui.hold("command"):
                pyautogui.press("r")
                self.login_fill()
        time.sleep(5)

        with pyautogui.hold("command"):
            pyautogui.press("t")
        time.sleep(2)
        pyautogui.write(self.config["quoting_url"], interval=0.1)
        pyautogui.press("enter")
        pyautogui.press("enter")
        time.sleep(2)

    def login_button_click(self) -> Dict:
        """
        点击首页的登录按钮
        :return: dict(kwargs, status=status, info=info)
        """
        return self._locate_and_click(f"{self.path}/staticfile/login_button.png")

    def login_fill(self):
        print("开始填充登录信息")
        form_location = pyautogui.locateOnScreen(
            f"{self.path}/staticfile/login_form_username.png", confidence=0.9
        )
        print("获取登录框坐标")
        username_point = pyautogui.center(form_location)
        pyautogui.click(username_point)
        print("输入用户名")
        pyautogui.write(self.config["username"], interval=0.1)
        pyautogui.press("tab")
        print("输入密码")
        pyautogui.write(self.config["passwd"], interval=0.1)

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
