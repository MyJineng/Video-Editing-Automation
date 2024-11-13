import pyautogui
import os
import time
import subprocess
import pygame
from datetime import datetime
from Config import (encoder_path, source_path, processed_path, music_file,
                    driver_path, email, password, send_to_list, email_message)
from WeTransfer import transfer

# Show all files in source path
original = source_path
all_files_and_dirs = os.listdir(original)
original_files = [f for f in all_files_and_dirs if os.path.isfile(os.path.join(original, f))]
print(original_files)
time.sleep(5)

# Starts 'Adobe Media Encoder.exe'
subprocess.Popen([encoder_path])
time.sleep(14)

# 1st click selects files to encode
pyautogui.click(676, 130)
pyautogui.click
time.sleep(1)

# 2nd click selects all files in folder
pyautogui.click(422, 232)
pyautogui.click
pyautogui.hotkey('ctrl', 'a')

# 3rd click confirms file upload
pyautogui.click(745, 617)
pyautogui.click
time.sleep(10)

# 4th/5th clicks select all files to encode
pyautogui.click(1048, 232)
pyautogui.hotkey('ctrl', 'a')
pyautogui.click(1167, 236)
time.sleep(2)

# 6th click searches for output folder
pyautogui.hotkey('ctrl', 'l')
pyautogui.write(processed_path)
pyautogui.press('enter')
time.sleep(5)

# 7th click selects output folder
pyautogui.click(726, 556)

# 8th click runs file conversion
pyautogui.click(1333, 128)
pyautogui.click
time.sleep(5)

all_files_and_dirs = os.listdir(processed_path)
processed_files = [f for f in all_files_and_dirs if os.path.isfile(os.path.join(processed_path, f))]

# Checks if files are in processed folder and if the temporary files still exist - aka are all files encoded
while len(processed_files) > 0 and any(file.endswith('.m4v') or file.endswith('.aac') for file in processed_files):
    time.sleep(25)
    all_files_and_dirs = os.listdir(processed_path)
    processed_files = [f for f in all_files_and_dirs if os.path.isfile(os.path.join(processed_path, f))]
    print(processed_files)

time.sleep(10)

# Renames each file to include today's date
now = datetime.now()
date = now.strftime("%m.%d.%Y")
for x in processed_files:
    base, ext = os.path.splitext(x)
    os.rename(rf'{processed_path}\{x}', rf'{processed_path}\{base}_{date}{ext}')

# Audio Notification that encoding is done
pygame.mixer.init()
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()

all_files_and_dirs = os.listdir(processed_path)
processed_files = [f for f in all_files_and_dirs if os.path.isfile(os.path.join(processed_path, f))]
print(f'Processed Files: {processed_files}')
cont = input('Please review and type "ok" to continue or "break" to stop: ')
if cont == 'ok':
    transfer(driver_path, email, password, send_to_list, email_message, processed_path, processed_files)
elif cont == 'break':
    pass


# The code below is to determine mouse click locations

# count = 0
# while True:
#     x, y = pyautogui.position()  # Get current mouse position
#     time.sleep(1)
#     count = count + 1
#     print(f"Current mouse position: x={x}, y={y}")
#     if count == 5:
#         break