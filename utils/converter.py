import pyautogui


def monitor():
    try:
        while True:
            x, y = pyautogui.position()
            print(x, y)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    monitor()