import time

import pyautogui

# Run this file and move your mouse over the spots you need.
# It prints the (x, y) position of the cursor every half second.
# Copy those numbers into the CONFIG section of 03_bot.py.
# Press Ctrl+C to stop.

try:
    while True:
        print(pyautogui.position())
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Stopped.")
