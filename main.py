import time
from service.marine_login import MarineLoginService
from service.marine_quoting import MarineQuotingService
from enum import Enum
import requests
from rich.console import Console
from rich.table import Table
from rich.progress import track


class Action(Enum):

    LOGIN = "login"
    QUOTING = "quoting"


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
    console.print(table)


def do_action(action: str):
    if action == Action.LOGIN.value:
        login_service = MarineLoginService()
        login_service.login_main()
    # goto quoting
    if action == Action.QUOTING.value:
        quoting_service = MarineQuotingService()
        quoting_service.quoting_main(quoting_service.config["departureFrom"])


def main():
    console = Console()
    try:
        rich_format()
        while True:
            for _ in track(range(10), description="正在等待下一次执行..."):
                time.sleep(1)
            try:
                action_resp = requests.get("11")
            except Exception as e:
                console.print(f"请求接口出现异常错误：{e}, 请重试，或者将报错信息发送给联系维护人确认原因")
                continue
            do_action(action_resp["label"])
    except KeyboardInterrupt:
        console.print(f"程序因人为 ctrl - c 操作退出，bye")


if __name__ == "__main__":
    do_action(action='quoting')
