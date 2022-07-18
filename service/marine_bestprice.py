import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from service.marine_status import MarineStatusService
from typing import Dict
import time
import pyperclip


class MarineBestPriceService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineBestPriceService, self).__init__()

    def read_page_data(self):
        info = [{}]
        pyautogui.click(x=65, y=272, clicks=2, interval=1)
        pyautogui.hotkey("command", "a")
        time.sleep(1)
        pyautogui.hotkey("command", "c")
        time.sleep(1)
        page_string = pyperclip.paste()
        for i in page_string.split("SPOTON"):
            if "综合利率" in i:
                print(i.replace("\n", ","))
