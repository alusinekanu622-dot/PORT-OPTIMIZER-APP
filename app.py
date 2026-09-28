import os
import sys
import threading
import webbrowser

APP_DIR = os.path.dirname(os.path.abspath(__file__))
INDEX = os.path.join(APP_DIR, "index.html")

def run():
    try:
        import webview
        webview.create_window(
            "Port Optimizer",
            INDEX,
            width=1400,
            height=900,
            min_size=(1000, 650),
            resizable=True
        )
        webview.start()
    except ImportError:
        # Fallback: open the same system in the default browser.
        webbrowser.open("file://" + INDEX.replace("\\", "/"))

if __name__ == "__main__":
    run()
