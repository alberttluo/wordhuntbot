import time
import pyautogui
import wordhuntsolverBASIC
import signal
from pynput.keyboard import Controller, Key

keyboard = Controller()
signal.alarm(82)
# signal.alarm(12)

def split(word):
    return [char for char in word]

def mouse_type(word):
    for i in split(word):
        keyboard.type(i)
        time.sleep(0.01)
    keyboard.press(Key.enter)
    time.sleep(0.01)
    keyboard.release(Key.enter)


def mouse_drag(coordinates):
    pyautogui.mouseUp()
    sx, sy = int(coordinates[0][0]), int(coordinates[0][1])


    pyautogui.moveTo(sx, sy, 0.0000000000001)
    pyautogui.mouseDown()


    for coordinate in coordinates[1:]:
        x, y = int(coordinate[0]), int(coordinate[1])
        pyautogui.moveTo(x, y, 0.0000001)

    pyautogui.mouseUp()

arrays = wordhuntsolverBASIC.get_coords()
poss_words = wordhuntsolverBASIC.get_poss_words()
drags = wordhuntsolverBASIC.get_drags()
sorter = sorted(arrays, key=len, reverse=True)
# with open("coordinate_paths.txt", "r") as file:
#     for line in file:
#         arrays.append(line.rstrip('\n'))

print(f'Words to go through: {len(arrays)}')
words_left = len(arrays)

# for coordinatep in arrays:
#     print(f'{words_left} words to go!')
#     words_left -= 1

#     mouse_drag(coordinatep)

#     time.sleep(0.00001)
    

# pyautogui.mouseUp()

for p in poss_words:
    print(p)
    mouse_type(p)
    time.sleep(0.1)
