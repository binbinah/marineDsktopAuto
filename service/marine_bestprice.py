# -*- coding: utf-8 -*-

import pyautogui
from utils.response_wrapper import func_resp_wrapper
from config.auto_config import MarineYamlConfig
from service.marine_status import MarineStatusService
from typing import Dict
import time
import pyperclip
from rich.console import Console


class MarineBestPriceService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineBestPriceService, self).__init__()

    def read_page_data(self):
        pyautogui.hotkey(
            self.locate_address_keymap[0], self.locate_address_keymap[1], interval=0.5
        )
        pyautogui.press("tab", interval=0.5)
        pyautogui.hotkey(self.cmd, "a", interval=0.5)
        pyautogui.hotkey(self.cmd, "c", interval=0.5)
        page_string = pyperclip.paste()
        for i in page_string.split("SPOTON"):
            if "综合利率" in i:
                print(i.replace("\n", ","))
            if "目前没有报价可供选择" in i:
                console = Console()
                console.print("Bingo！命中一个待放仓的线路，请关注", style="bold red")
