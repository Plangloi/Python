import time
import pygetwindow as gw
import pyautogui

# Function to find window by title
def find_window(title):
    try:
        window = gw.getWindowsWithTitle(title)[0]
        return window
    except IndexError:
        return None

# Open System Preferences
system_prefs = find_window("System Preferences")
if system_prefs:
    system_prefs.activate()

    # Open Displays
    time.sleep(1)
    displays = find_window("Displays")
    if displays:
        displays.activate()

        # Switch to Arrangement tab
        time.sleep(1)
        pyautogui.hotkey('command', '1')  # Assuming Arrangement tab is the first one

        # Check "Mirror Displays"
        time.sleep(1)
        pyautogui.press('space')

        # Close System Preferences
        time.sleep(1)
        system_prefs.close()
    else:
        print("Error: 'Displays' window not found.")
else:
    print("Error: 'System Preferences' window not found.")
