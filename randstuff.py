import pyautogui

while True:
    # Get the current mouse position
    x, y = pyautogui.position()

    # Print the coordinates
    print(f"Mouse coordinates: X={x}, Y={y}")
