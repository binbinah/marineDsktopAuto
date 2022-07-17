import pyautogui


def monitor():
    this_x = 0
    this_y = 0
    try:
        while True:
            x, y = pyautogui.position()
            if this_x == x and this_y == y:
                continue
            this_y = y
            this_x = x
            print(this_x,this_y)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    monitor()
    print(pyautogui.size())
    # 1680,1050 分辨率 (0.1345)
    # 浏览器地址栏坐标：226,85
    #

