# electron_bridge.py
import webview
import subprocess
import sys
import os

class API:
    def open_url(self, url):
        """使用系统默认方式打开URL"""
        try:
            if sys.platform.startswith('win'):
                # Windows系统使用os.startfile
                os.startfile(url)
            elif sys.platform.startswith('darwin'):
                # macOS系统使用open命令
                subprocess.call(['open', url])
            else:
                # Linux系统使用xdg-open命令
                subprocess.call(['xdg-open', url])
        except Exception as e:
            print(f"打开链接失败: {e}")

def create_window():
    api = API()
    webview.create_window(
        '爱眼城数字化工作平台',
        'index.html',  # 主HTML文件路径
        js_api=api,
        width=1200,
        height=800,
        resizable=True,
        fullscreen=False
    )
    webview.start(debug=True)

if __name__ == '__main__':
    create_window()