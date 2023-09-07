# check the person's salary for the current fiscal year and month. This script should run on the first of each month to give a monthly update on their salary


import pyautogui
import subprocess
import time

from datetime import datetime


# # 'current_date.year' 'current_date.month' 'current_date.day'
# current_date = date.today()
# # print(f"It is day {current_date.day} of the month of {current_date.month} in the year {current_date.year}.")

ts = datetime.now()
str_timestamp = f'{ts:%Y-%m-%d--%H-%M-%S}--[YMD-hms]'

time.sleep(1)
subprocess.Popen("start chrome /incognito https://open.alabama.gov/Checkbook/Payee/Default.aspx", shell=True)    # opens a new Chrome window

time.sleep(1)
pyautogui.write('')

time.sleep(1)
pyautogui.press('tab')

time.sleep(1)
pyautogui.press('enter')        # submit name to search 

time.sleep(11)          # wait for search results




# press shift-tab 12 times to select the name, then press enter
pyautogui.keyDown('shift')
for tab in range(12):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"name tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')

# shift-tab to personnel costs and press enter
pyautogui.keyDown('shift')
for tab in range(13):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"personnel costs tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')


# gross pay and press enter
pyautogui.keyDown('shift')
for tab in range(13):   
    time.sleep(1)
    pyautogui.press('tab')
    print(f"name tab {tab}")

time.sleep(1)
pyautogui.keyUp('shift')
time.sleep(1)
print(f"enter")
pyautogui.press('enter')


# press tab 11 times to select download excel, then press enter. This opens a Save As window
for tab in range(11):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"excel tab {tab}")

time.sleep(1)
pyautogui.press('enter')    # opens 'Save As' window

# clear filename, then use timestamp for excel filename
time.sleep(5)
print("before backspace")
pyautogui.press('backspace')

time.sleep(1)
print("before write")
pyautogui.write(str_timestamp)
print(f"filename {str_timestamp}")



time.sleep(1)
pyautogui.keyDown('shift')

# select left side nav bar
time.sleep(1)
for tab in range(3):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"SaveAs 1 - {tab}")

pyautogui.keyUp('shift')
time.sleep(1)

# select 'SCRIPT_OUTPUT' on left side nav bar and press enter
pyautogui.press('down')
time.sleep(1)
pyautogui.press('enter')


# press tab to select save, then press enter
time.sleep(1)
for tab in range(6):
    time.sleep(1)
    pyautogui.press('tab')
    print(f"ClickSave - {tab}")

time.sleep(1)
pyautogui.press('enter')    # press enter to save excel file








# active_window = pyautogui.getActiveWindow()
# active_window.minimize()



# pyautogui.press('tab')
# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# pyautogui.press('down')


# pyautogui.click(591, 521)