# -*- coding: utf-8 -*-

import time
from service.marine_login import MarineLoginService
from service.marine_quoting import MarineQuotingService
from service.marine_status import MarineStatusService
from service.marine_bestprice import MarineBestPriceService
from rich.console import Console
from rich.table import Table
from rich.progress import track
from config.auto_config import Action
import re
from utils.converter import month_convert
from datetime import datetime, timedelta


def rich_format():
    """
    格式化显示
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("使用说明", width=100)
    table.add_row("自动化程序会占用键盘和鼠标以及屏幕。")
    table.add_row("注意事项：")
    table.add_row("1、请确保[red]窗口焦点在 Chrome 浏览器上[/red]")
    table.add_row("3、如退出自动化程序，请按：ctrl-c")
    console.print(table)


def do_action(action: str, the_date, monitor_result):
    if action == Action.LOGIN.value:
        login_service = MarineLoginService()
        return login_service.login_main()
    # goto quoting
    if action == Action.QUOTING.value:
        month_pair = month_convert()
        the_date_list = the_date.split("-")
        the_date_list[1] = month_pair[the_date_list[1]]
        quoting_service = MarineQuotingService("-".join(the_date_list))
        return quoting_service.quoting_main()

    # goto bestpricee
    if action == Action.BEST_PRICE.value:
        best_price = MarineBestPriceService()
        return best_price.read_page_data(the_date, monitor_result)


def main():
    console = Console()
    try:
        rich_format()

        input_date = input(
            "请输入你想要监控的日期（格式示例：YYYY-MM-DD），如果直接回车或者输入的日期无效，默认监控明天的报价情况。\n请输入："
        )
        date_match_result = re.search(r"(\d{4}-\d{1,2}-\d{1,2})", input_date)
        try:
            input_date_reg = date_match_result.group(0)
        except AttributeError:
            input_date_reg = None
        if input_date and input_date_reg:
            if datetime.strptime(input_date, "%Y-%m-%d") < datetime.today():
                the_date = datetime.today().strftime("%d-%m-%Y")
                console.print("输入的日期早于今天，自动调整为监控今天的报价")
            else:
                the_date = datetime.strptime(input_date, "%Y-%m-%d").strftime(
                    "%d-%m-%Y"
                )
        else:
            the_date = (datetime.now() + timedelta(1)).strftime("%d-%m-%Y")

        for _ in track(range(10), description="请在进度条完成之前，将 Chrome 置于前台，并且打开首页..."):
            time.sleep(1)
        marine_status_service = MarineStatusService()
        while True:
            for _ in track(range(5), description="即将进行下一步自动化操作..."):
                time.sleep(1)

            address = marine_status_service.read_chrome_address()
            try:
                status = marine_status_service.action_pair[address]
            except KeyError:
                status = Action.LOGIN.value
            try:
                info = do_action(status, the_date, marine_status_service.monitor_result)
                if info:
                    marine_status_service.monitor_result.update(info)

            except Exception as e:
                console.print(f"执行失败，错误信息:{e}")
    except KeyboardInterrupt:

        n = 5
        while n > 0:
            console.print(f"\n程序将在 {n} 秒后退出...")
            time.sleep(1)
            n = n - 1
        console.print(f"\n程序因人为 ctrl - c 操作退出，bye", style="green")


if __name__ == "__main__":
    main()
