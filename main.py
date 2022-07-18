import time
from service.marine_login import MarineLoginService
from service.marine_quoting import MarineQuotingService
from service.marine_status import MarineStatusService
from rich.console import Console
from rich.table import Table
from rich.progress import track
from config.auto_config import Action


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
    table.add_row("4、需要 Chrome 插件：油猴插件 + Keyboard Shortcuts to Close Other/Right Tabs")
    console.print(table)


def do_action(action: str):
    if action == Action.LOGIN.value:
        login_service = MarineLoginService()
        login_service.login_main()
    # goto quoting
    if action == Action.QUOTING.value:
        quoting_service = MarineQuotingService()
        quoting_service.quoting_main(quoting_service.config["departureFrom"])

    # goto bestpricee
    if action == Action.BEST_PRICE.value:
        pass


def main():
    console = Console()
    try:
        rich_format()
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
                do_action(status)
            except Exception:
                console.print("执行失败，请将浏览器全屏，并且将本程序最小化运行")
    except KeyboardInterrupt:
        console.print(f"程序因人为 ctrl - c 操作退出，bye")


if __name__ == "__main__":
    main()
