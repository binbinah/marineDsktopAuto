import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from rich import print
from typing import Dict


class MarineLoginService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineLoginService, self).__init__()

    def login_button_click(self) -> Dict:
        """
        点击首页的登录按钮
        :return: dict(kwargs, status=status, info=info)
        """
        return self._locate_and_click(f"{self.path}/staticfile/login_button.png")

    def login_fill(self):
        click_r = self._locate_and_click(f"{self.path}/staticfile/login_form_user.png")
        if not click_r['status']:
            return click_r['info']
        pyautogui.write('Hello world!', interval=0.25)

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
            return func_resp_wrapper(status=False, info=f"没有找到{path.split('/')[-1]}，需要确认页面是否存在该图片锚点。")


if __name__ == "__main__":
    click_service = MarineLoginService()
    resp = click_service.login_fill()
    print(resp)
