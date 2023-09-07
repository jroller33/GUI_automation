
import pyautogui
import subprocess
import time
import random

from datetime import datetime

ts = datetime.now()
timestamp_str = f'{ts:%Y-%m-%d--%H-%M-%S}--[YMD-hms]'

run_count = 0

first_name_list = ["Tom", "Jason", "Larry", "Reginald", "Helene", "Esther"]

last_name_list = ["Jenkins", "Warnix", "Goodgame", "Beauregard", "Jones", "Patel"]

def generate_random_date(input):
    random_month = random.choice(range(1, 13))
    random_day = random.choice(range(1, 29))

    if input == "child":
        random_year = random.choice(range(2013, 2019))
    if input == "parent":
        random_year = random.choice(range(1970, 1990))

    if len(str(random_day)) < 2:
        random_day = f"0{random_day}"


    date_string = f"{random_month} - {random_day} = {random_year}"
    return date_string






try:
    while run_count < 100:      # run_count starts at 0 and goes up to 99
        print(f"[***] Starting new run at run_count: {run_count}")

        first_name = random.choice(first_name_list)
        last_name = random.choice(last_name_list)
        gender = random.choice(range(1, 4))

        child_DOB = generate_random_date("child")

# https://www.geeksforgeeks.org/python-generate-k-random-dates-between-two-other-dates/#

        applying_for_year = random.choice(range(1,3))
        applying_for_grade = random.choice(range(1,13))

        print(f"[*] Child DOB: {child_DOB}")

        # print(f"[*] first_name: {first_name}\n\t last_name: {last_name}\n\t gender: {gender}")

        # time.sleep(1)
        # subprocess.Popen("start chrome /incognito https://portals.veracross.com/aidan/form/general_inquiry", shell=True)    # opens a new incognito Chrome window

        # time.sleep(5)
        # pyautogui.press('tab')

        # time.sleep(1)
        # pyautogui.write('')




        run_count += 1
except KeyboardInterrupt:
    print(f"[!] Script exited at run_count: {run_count}")


# time.sleep(1)
# pyautogui.write('')

# time.sleep(1)
# pyautogui.press('tab')

# time.sleep(1)
# pyautogui.press('enter')        # submit name to search 

# time.sleep(11)          # wait for search results


# # press shift-tab 12 times to select the name, then press enter
# pyautogui.keyDown('shift')
# for tab in range(12):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"name tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')

# # shift-tab to personnel costs and press enter
# pyautogui.keyDown('shift')
# for tab in range(13):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"personnel costs tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')


# # gross pay and press enter
# pyautogui.keyDown('shift')
# for tab in range(13):   
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"name tab {tab}")

# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# print(f"enter")
# pyautogui.press('enter')


# # press tab 11 times to select download excel, then press enter. This opens a Save As window
# for tab in range(11):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"excel tab {tab}")

# time.sleep(1)
# pyautogui.press('enter')    # opens 'Save As' window

# # clear filename, then use timestamp for excel filename
# time.sleep(5)
# print("before backspace")
# pyautogui.press('backspace')

# time.sleep(1)
# print("before write")
# pyautogui.write(str_timestamp)
# print(f"filename {str_timestamp}")


# time.sleep(1)
# pyautogui.keyDown('shift')

# # select left side nav bar
# time.sleep(1)
# for tab in range(3):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"SaveAs 1 - {tab}")

# pyautogui.keyUp('shift')
# time.sleep(1)

# # select 'SCRIPT_OUTPUT' on left side nav bar and press enter
# pyautogui.press('down')
# time.sleep(1)
# pyautogui.press('enter')


# # press tab to select save, then press enter
# time.sleep(1)
# for tab in range(6):
#     time.sleep(1)
#     pyautogui.press('tab')
#     print(f"ClickSave - {tab}")

# time.sleep(1)
# pyautogui.press('enter')    # press enter to save excel file








# active_window = pyautogui.getActiveWindow()
# active_window.minimize()



# pyautogui.press('tab')
# time.sleep(1)
# pyautogui.keyUp('shift')
# time.sleep(1)
# pyautogui.press('down')


# pyautogui.click(591, 521)