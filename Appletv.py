import time
import pyautogui

# Adjust these coordinates based on your screen resolution
system_prefs_icon = (100, 100)
displays_icon = (150, 300)
arrangement_tab = (300, 200)
mirror_displays_checkbox = (500, 400)

# Open System Preferences
pyautogui.click(system_prefs_icon)
time.sleep(1)

# Open Displays
pyautogui.click(displays_icon)
time.sleep(1)

# Switch to Arrangement tab
pyautogui.click(arrangement_tab)
time.sleep(1)

# Check "Mirror Displays"
pyautogui.click(mirror_displays_checkbox)

# Close System Preferences
pyautogui.hotkey('command', 'q')
