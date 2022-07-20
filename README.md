# marineDsktopAuto
一个桌面自动化项目。

其中，依赖根据不同 OS 会有不同的依赖要求，本项目主要在 macOS 下开发，运行主要在 Windows，因此不适合直接导入 requirements.txt

主要安装依赖：
其他具体需要的直接在 Windows 下看情况安装。

```
pip install pyautugui
pip install rich
pip install pyinstaller
pip install black
pip install opencv-python
pip install pyyaml

pip install pywin32
```

如果在 Windows 下运行，参考的获取窗口句柄代码为：

```
import sys
import win32gui
import win32con


def get_all_hwnd(hwnd, mouse):
    if (win32gui.IsWindow(hwnd)
            and win32gui.IsWindowEnabled(hwnd)
            and win32gui.IsWindowVisible(hwnd)):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})


hwnd_title = {}
win32gui.EnumWindows(get_all_hwnd, 0)
for h, t in hwnd_title.items():
    if t :
        print (h, t)   
```


#### 完全体结构：
![image](https://user-images.githubusercontent.com/5344741/179388723-51f80972-ba87-497b-a52d-3a8b43c1ef3e.png)
