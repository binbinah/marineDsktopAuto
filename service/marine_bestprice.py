# -*- coding: utf-8 -*-
import time

import pyautogui
import rich

from config.auto_config import MarineYamlConfig
from rich.table import Table
import pyperclip
from rich.console import Console
import os
from utils.marineConsoleRequest import ConsoleRequest


class MarineBestPriceService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineBestPriceService, self).__init__()

    def read_page_data(self, the_date):
        with pyautogui.hold(self.locate_address_keymap[0]):
            pyautogui.press(self.locate_address_keymap[1])
        pyautogui.press("tab", interval=0.5)
        with pyautogui.hold(self.cmd):
            pyautogui.press("a")
        time.sleep(0.5)
        with pyautogui.hold(self.cmd):
            pyautogui.press("c")
        page_string = pyperclip.paste()
        post_data = []
        console = Console()
        for i in page_string.split("SPOTON"):
            if "综合利率" in i:
                i = i.replace(f"最早到达{os.linesep}最早离港时间{os.linesep}", "")
                start = ",".join(i.split(os.linesep)[0:2])
                info = ",".join(i.split(os.linesep)[2:6])
                end = ",".join(i.split(os.linesep)[6:9])
                cost = ",".join(i.split(os.linesep)[9:12])
                monitor_type = "could"
                post_data.append([start, info, end, cost, monitor_type])

            if "目前没有报价可供选择" in i:
                i = i.replace(f"最早到达{os.linesep}最早离港时间{os.linesep}", "")
                start = ",".join(i.split(os.linesep)[0:2])
                info = ",".join(i.split(os.linesep)[2:6])
                end = ",".join(i.split(os.linesep)[6:9])
                cost = ",".join(i.split(os.linesep)[9:12])
                monitor_type = "waiting"
                post_data.append([start, info, end, cost, monitor_type])

        if post_data:
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("序号", width=5)
            table.add_column("时间和起始港")
            table.add_column("详细信息")
            table.add_column("时间和卸货港")
            table.add_column("价格")
            for key, post_item in enumerate(post_data):
                table.add_row(
                    str(key), post_item[0], post_item[1], post_item[2], post_item[3]
                )

                req = ConsoleRequest()

                req_data = {
                    "monitor_time": the_date,
                    "monitor_type": "could",
                    "port_of_loading": post_item[0],
                    "port_of_discharge": post_item[2],
                    "container_detail": post_item[1],
                    "email_status": True,
                    "is_active": True,
                }
                rich.print(req_data)
                req.send_request(req_data)

            console.print(table)

        else:
            console.print("今日暂无可选择的舱位", style="bold red")
