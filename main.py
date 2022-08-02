# -*- coding: utf-8 -*-

import time
from service.marine_login import MarineLoginService
from service.marine_quoting import MarineQuotingService
from service.marine_bestprice import MarineBestPriceService
from config.auto_config import MarineYamlConfig
from rich.console import Console
from rich.table import Table
from rich.progress import track
from config.auto_config import Action
import re
from utils.converter import month_convert
from datetime import datetime, timedelta
import pyautogui
import pyperclip
from rich.prompt import Prompt


def rich_format():
    """
    格式化显示
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("使用说明", width=100)
    table.add_row("自动化程序会占用键盘和鼠标以及屏幕。")
    table.add_row("注意事项：")
    table.add_row("1、请确保[red]窗口焦点在 Chrome 浏览器上[/red]，并且网站语言调整为：[red]中文。[/red]")
    table.add_row("3、如退出自动化程序，请按：ctrl-c")
    console.print(table)


class MarineMain(MarineYamlConfig):
    def __init__(self, **kwargs):
        super(MarineMain, self).__init__()
        self.host = kwargs.get("host")
        self.port_of_loading = kwargs.get("port_of_loading")
        self.port_of_discharge = kwargs.get("port_of_discharge")
        self.input_date = kwargs.get("input_date")
        self.weight = kwargs.get("weight")
        self.console = Console()
        self.monitor_result = {self._input_date(): ""}
        self.action_pair = {
            self.config["quoting_url"].format(host=self.host): Action.QUOTING.value,
            self.config["cnc_line_url"].format(host=self.host): Action.QUOTING.value,
            self.config["cnc_in"].format(host=self.host): Action.QUOTING.value,
            self.config["best_price"].format(host=self.host): Action.BEST_PRICE.value,
            self.config["no_result"].format(host=self.host): Action.NO_RESULT.value,
            self.config["modify_url"].format(host=self.host): Action.MODIFY_URL.value,
        }

    def do_action(self, action: str):
        if action == Action.LOGIN.value:
            login_service = MarineLoginService(host=self.host)
            return login_service.login_main()
        # goto quoting
        if action == Action.QUOTING.value:
            month_pair = month_convert()
            the_date_list = self._input_date().split("-")
            the_date_list[1] = month_pair[the_date_list[1]]
            quoting_service = MarineQuotingService(
                host=self.host,
                the_date="-".join(the_date_list),
                port_of_loading=self._port_of_loading(),
                port_of_discharge=self._port_of_discharge(),
                weight=self.weight,
            )
            return quoting_service.quoting_main()

        # goto bestpricee
        if action == Action.BEST_PRICE.value:
            best_price = MarineBestPriceService()
            self.monitor_result = best_price.read_page_data(
                self._input_date(), self.monitor_result
            )

        # goto modify_url
        if action == Action.MODIFY_URL.value:
            with pyautogui.hold(self.cmd):
                pyautogui.press("f")
            pyperclip.copy('获取我的报价')
            with pyautogui.hold(self.cmd):
                pyautogui.press("v")
            pyautogui.press("enter", interval=0.5)
            pyautogui.press("esc", interval=0.5)
            pyautogui.press("enter", interval=0.5)
            time.sleep(5)

        # goto no result
        if action == Action.NO_RESULT.value:
            self.console.print("没有查询到相关数据，请检查输入的参数是否正确！", style="red")
            raise Exception("没有查询到相关数据，请检查输入的参数是否正确！")

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

    def _port_of_discharge(self):
        """
        验证输入的参数是否合法
        """
        try:
            return self.port_of_discharge.split(" ")[0]
        except Exception:
            return self.config["portOfDischarge"]

    def _port_of_loading(self):
        """
        验证输入的参数是否合法
        """
        try:
            return self.port_of_loading.split(" ")[0]
        except Exception:
            return self.config["portOfLoading"]

    def _input_date(self):
        """
        验证输入的参数是否合法
        """
        date_match_result = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", self.input_date)
        try:
            input_date_reg = date_match_result.group(0)
        except AttributeError:
            input_date_reg = None
        if self.input_date and input_date_reg:
            if datetime.strptime(self.input_date, "%Y-%m-%d") < datetime.today():
                the_date = datetime.today().strftime("%d-%m-%Y")
            else:
                the_date = datetime.strptime(self.input_date, "%Y-%m-%d").strftime(
                    "%d-%m-%Y"
                )
        else:
            the_date = (datetime.now() + timedelta(1)).strftime("%d-%m-%Y")
        return the_date


def main():
    console = Console()

    try:
        rich_format()
        host = Prompt.ask("请填写 host ,默认：",choices=['www.cnc-line.com', 'www.cma-cgm.com'], default="www.cnc-line.com")
        port_of_loading = Prompt.ask("请输入装货港,默认：", default="NINGBO")
        port_of_discharge = Prompt.ask("请输入卸货港，默认：", default="JAKARTA")
        input_date = Prompt.ask(
            "请输入离港日期，默认：", default=(datetime.today() + timedelta(1)).strftime("%Y-%m-%d")
        )
        weight = Prompt.ask("请输入净重，默认：", default="12000")
        input_value_pair = dict(
            host=host,
            port_of_loading=port_of_loading,
            port_of_discharge=port_of_discharge,
            input_date=input_date,
            weight=weight,
        )

        marine_main = MarineMain(**input_value_pair)

        for _ in track(range(10), description="请在进度条完成之前，将 Chrome 置于前台，并且打开首页..."):
            time.sleep(1)
        while True:
            for _ in track(range(5), description="即将进行下一步自动化操作..."):
                time.sleep(1)

            address = marine_main.read_chrome_address()
            try:
                status = marine_main.action_pair[address]
            except KeyError:
                status = Action.LOGIN.value
            try:
                marine_main.do_action(status)

            except Exception as e:
                console.print(f"执行失败，错误信息:{e}")
                break
    except KeyboardInterrupt:

        n = 5
        while n > 0:
            console.print(f"\n程序将在 {n} 秒后退出...")
            time.sleep(1)
            n = n - 1
        console.print(f"\n程序因人为 ctrl - c 操作退出，bye", style="green")


if __name__ == "__main__":
    main()
