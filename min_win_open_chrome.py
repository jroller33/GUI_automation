import pyautogui
import subprocess
import time

active_window = pyautogui.getActiveWindow()

active_window.minimize()

time.sleep(5)

subprocess.Popen("start chrome", shell=True)    # opens a new Chrome window