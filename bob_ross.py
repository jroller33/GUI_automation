# on Windows, this script paints a spiral

import subprocess
import pyautogui
import time

window_size = pyautogui.size()
mid_window_width = (window_size[0] / 2)
mid_window_height = (window_size[1] / 2)

pyautogui.moveTo(mid_window_width, mid_window_height, duration=1)   # moves mouse to center screen

subprocess.Popen("mspaint", shell=True)    # opens a new Paint window


# print(window_size)
# print(f"half width: {mid_window_width} \n half height: {mid_window_height}")


time.sleep(5)
pyautogui.click()
distance = 300
change = 20
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.2)   # move right
    distance = distance - change

    pyautogui.drag(0, distance, duration=0.2)   # move down
    pyautogui.drag(-distance, 0, duration=0.2)  # move left
    distance = distance - change
    pyautogui.drag(0, -distance, duration=0.2)  # move up

