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

    @staticmethod
    def read_chrome_address():
        """
        读取浏览器 URL 地址
        """
        pyautogui.click(x=226, y=85, clicks=2)
        pyautogui.hotkey("command", "a", interval=0.5)
        pyautogui.hotkey("command", "c", interval=0.5)
        address = pyperclip.paste()
        return address


if __name__ == "__main__":
    time.sleep(3)
    marine_status_service = MarineStatusService()
    marine_status_service.read_chrome_address()
    print(marine_status_service.read_chrome_address())
