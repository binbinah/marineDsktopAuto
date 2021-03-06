# marineDesktopAuto

#### 本客户端只能针对特定的场景进行自动化，不具备通用型。更多可以参考 pyautogui 文档去实现特定需求下的自动化。

依赖根据不同 OS 会有不同的依赖要求，本项目主要在 macOS 下开发，运行主要在 Windows，因此不适合直接导入 requirements.txt

主要安装依赖：

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

对于如何获取浏览器被选择的文本的坐标，纯 js 有如下实现方式：

1. 打开控制台：输入 下方脚本，可以将网页中被选择的文本的坐标复制到剪贴板 (**需要注意的是，通过 js 获取的坐标，是基于浏览器 Window 或者 document 的，和显示器坐标不一样，因此，这个方法适合基于 js，比如油猴脚本的浏览器自动化。**)

```
function copyToClipboard(text) {
    var dummy = document.createElement("textarea");
    document.body.appendChild(dummy);
    dummy.value = text;
    dummy.select();
    document.execCommand("copy");
    document.body.removeChild(dummy);
}
const selectedText = window.getSelection().getRangeAt(0).getBoundingClientRect();
copyToClipboard('{x:'+selectedText.x+',y:'+selectedText.y+'}')


```


#### 完全体结构：
![image](https://user-images.githubusercontent.com/5344741/180478023-0412d248-bac0-4ba9-96ac-085cde36c8c2.png)

