
"""
자산관리 매니저
실행: python main.py
빌드: pyinstaller --onefile --windowed --add-data "index.html;." --name "AssetsManager" main.py
"""

import os
import sys
import webview

# EXE 빌드 시 파일 경로 처리
if getattr(sys, 'frozen', False):
    BASE_DIR = sys._MEIPASS
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_FILE = os.path.join(BASE_DIR, "index.html")

if __name__ == "__main__":
    webview.create_window(
        title="💰 자산관리 매니저",
        url=f"file:///{HTML_FILE.replace(os.sep, '/')}",
        width=1200,
        height=800,
        min_size=(800, 600),
        resizable=True,
    )
    webview.start()