# -*- coding: utf-8 -*-
import time

import pyautogui
from config.auto_config import MarineYamlConfig
from rich.table import Table
import pyperclip
from rich.console import Console
import os
from utils.notification import Email


class MarineBestPriceService(MarineYamlConfig):
    """
    点击事件类
    """

    def __init__(self):
        super(MarineBestPriceService, self).__init__()

    def read_page_data(self, the_date, monitor_result):
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

            mail_body = ""

            for key, post_item in enumerate(post_data):
                table.add_row(
                    str(key), post_item[0], post_item[1], post_item[2], post_item[3]
                )
                mail_body += (
                    f"<p>时间和起始港：{post_item[0]}</p>"
                    f"<p>详细信息：{post_item[1]}</p>"
                    f"<p>时间和卸货港：{post_item[2]}</p>"
                    f"<p>价格：{post_item[3]}</p>"
                    f"<p>----</p>"
                )

            if mail_body != monitor_result[the_date]:
                console.print(table)

                email = Email(
                    gmail_from=self.config["mail_from"],
                    send_to=self.config["mail_to"],
                    gmail_smtp_key=self.config["mail_key"],
                )
                email.send(
                    subject=f"{the_date}监控结果",
                    content=mail_body,
                )
            else:
                console.print(f"{the_date}监控结果：无变化")
            monitor_result[the_date] = mail_body

        else:
            console.print("今日暂无可选择的舱位", style="bold red")

        with pyautogui.hold(self.locate_address_keymap[0]):
            pyautogui.press(self.locate_address_keymap[1])
        pyperclip.copy(self.config["cnc_line_url"])
        with pyautogui.hold(self.cmd):
            pyautogui.press("v")
        pyautogui.press("enter")
        return monitor_result


#         with pyautogui.hold(self.cmd):
#             pyautogui.press("f")
#         pyperclip.copy("修改搜索")
#         with pyautogui.hold(self.cmd):
#             pyautogui.press("v")
#         pyautogui.press("esc", interval=0.5)
#         with pyautogui.hold(self.console_keymap[0]):
#             with pyautogui.hold(self.console_keymap[1]):
#                 pyautogui.press(self.console_keymap[2])
#         time.sleep(0.5)
#         pyperclip.copy(
#             """function copyToClipboard(text) {
#     var dummy = document.createElement("textarea");
#     document.body.appendChild(dummy);
#     dummy.value = text;
#     dummy.select();
#     document.execCommand("copy");
#     document.body.removeChild(dummy);
# }
# const selectedText = window.getSelection().getRangeAt(0).getBoundingClientRect();
# copyToClipboard('{"x":'+selectedText.x+',"y":'+selectedText.y+'}')"""
#         )
#         time.sleep(0.5)
#         with pyautogui.hold(self.cmd):
#             pyautogui.press("v")
#         time.sleep(0.5)
#         pyautogui.press("enter", interval=0.5)
#         time.sleep(0.5)
#         coordinate = pyperclip.paste()
#         print(coordinate)
#         print(type(coordinate))
#         x_y = json.loads(str(coordinate))
#         with pyautogui.hold(self.console_keymap[0]):
#             with pyautogui.hold(self.console_keymap[1]):
#                 pyautogui.press(self.console_keymap[2])
#         print(x_y)
#         pyautogui.moveTo(x_y["x"], x_y["y"], duration=10)
#         pyautogui.click(x_y["x"] + 1, x_y["y"] + 1, clicks=2, interval=0.5)
