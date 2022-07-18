import pyautogui
import time


def month_convert():
    return {
        "01": "一月",
        "02": "二月",
        "03": "三月",
        "04": "四月",
        "05": "五月",
        "06": "六月",
        "07": "七月",
        "08": "八月",
        "09": "九月",
        "10": "十月",
        "11": "十一月",
        "12": "十二月",
    }


def monitor():
    this_x = 0
    this_y = 0
    try:
        while True:
            time.sleep(1)
            x, y = pyautogui.position()
            if this_x == x and this_y == y:
                continue
            this_y = y
            this_x = x
            print(this_x, this_y)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    monitor()
    print(pyautogui.size())
    # 1680,1050 分辨率 (0.1345)
    # 浏览器地址栏坐标：226,85
    #
