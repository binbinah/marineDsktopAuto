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
    table.add_row("自动化程序会占用键盘和鼠标以及屏幕，屏幕尺寸最好为：")
    table.add_row("注意事项：")
    table.add_row("1、将电脑全局输入法设置为[red]英文输入法[/red]")
    table.add_row("2、将浏览器最大化展示，将本应用程序的终端最小化")
    table.add_row("3、如需退出自动化程序，请按：ctrl-c")
    table.add_row("4、本程序运行的最优屏幕分辨率为：Size(width=1920, height=1080)")
    table.add_row("4、需要 Chrome 插件: Keyboard Shortcuts to Close Other/Right Tabs")
    console.print(table)


def do_action(action: str, the_date):
    if action == Action.LOGIN.value:
        login_service = MarineLoginService()
        login_service.login_main()
    # goto quoting
    if action == Action.QUOTING.value:
        month_pair = month_convert()
        the_date_list = the_date.split("-")
        the_date_list[1] = month_pair[the_date_list[1]]
        quoting_service = MarineQuotingService("-".join(the_date_list))
        quoting_service.quoting_main()

    # goto bestpricee
    if action == Action.BEST_PRICE.value:
        best_price = MarineBestPriceService()
        best_price.read_page_data()


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
            the_date = datetime.strptime(input_date, "%Y-%m-%d").strftime("%d-%m-%Y")
        else:
            the_date = (datetime.now() + timedelta(1)).strftime("%d-%m-%Y")

        for _ in track(range(10), description="请在进度条完成之前，将 Chrome 置于前台，并且打开首页..."):
            time.sleep(1)
        while True:
            for _ in track(range(5), description="即将进行下一步自动化操作..."):
                time.sleep(1)
            marine_status_service = MarineStatusService()
            address = marine_status_service.read_chrome_address()
            try:
                status = marine_status_service.action_pair[address]
            except KeyError:
                status = Action.LOGIN.value
            try:
                do_action(status, the_date)
            except Exception:
                console.print("执行失败，请将浏览器全屏，并且将本程序最小化运行")
    except KeyboardInterrupt:
        console.print(f"\n程序因人为 ctrl - c 操作退出，bye", style="green")


if __name__ == "__main__":
    main()
