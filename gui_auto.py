import pyautogui
import subprocess
import time

# wh = pyautogui.size()

# for i in range(2):
#     pyautogui.moveTo(100, 100, duration=0.5)
#     pyautogui.moveTo(200, 100, duration=0.5)
#     pyautogui.moveTo(200, 200, duration=0.5)
#     pyautogui.moveTo(100, 200, duration=0.5)

# pyautogui.mouseInfo()

# pyautogui.click(1773,26)    # minimizes vscode window if it's maximized

active_window = pyautogui.getActiveWindow()

active_window.minimize()

time.sleep(5)

subprocess.Popen("start chrome", shell=True)    # opens a new Chrome window