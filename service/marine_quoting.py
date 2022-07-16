import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from rich import print
import pyperclip
import time


class MarineQuotingService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineQuotingService, self).__init__()

    def quoting_main(self, date: str):
        pyautogui.position()
        pyautogui.click(x=65, y=272, clicks=2,interval=1)
        pyautogui.press("tab", presses=2, interval=1)
        self._fill_form(self.config["portOfLoading"])
        pyautogui.press("tab")
        self._fill_form(self.config["portOfDischarge"])
        pyautogui.press("tab", presses=2, interval=0.1)
        pyperclip.copy(date)
        pyautogui.hotkey("command", "v")
        pyautogui.press("enter", interval=1)
        pyautogui.press("tab", interval=1)
        pyautogui.press("down", interval=1,presses=4)
        pyautogui.press("enter", interval=1)
        pyautogui.press("tab", presses=2, interval=1)
        pyautogui.write(self.config["weight"], interval=0.1)
        pyautogui.press("tab", presses=4, interval=1)
        pyautogui.press("down", presses=2, interval=1)
        pyautogui.press("enter", interval=1)
        pyautogui.press("tab", presses=1, interval=1)
        pyautogui.press("enter", interval=1)

    def _fill_form(self, content):
        pyautogui.write(content)
        time.sleep(1)
        pyautogui.press("down", interval=1)
        pyautogui.press("enter", interval=1)

    def monitor(self):
        """ """
        try:
            while True:
                x, y = pyautogui.position()
                print(x, y)
        except KeyboardInterrupt:
            pass

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
    quoting = MarineQuotingService()
    quoting.quoting_main("16-七月-2022")
