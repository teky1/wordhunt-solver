import time

import pyautogui

import solver

top_leftX, top_leftY = 630, 480
tile_size = 70

pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0.1
pyautogui.MINIMUM_SLEEP = 0.01

def goto(coord, drag=True, duration=0.03):
    
    if drag:
        pyautogui.dragTo(
            top_leftX+tile_size*coord[1],
            top_leftY+tile_size*coord[0],
            duration,
            button="left",
            mouseDownUp=False
        )
    else:
        pyautogui.moveTo(
            top_leftX+tile_size*coord[1],
            top_leftY+tile_size*coord[0],
            duration,
        )

def do_word(letter_coords):
    goto(letter_coords[0], drag=False)
    pyautogui.mouseDown()

    for letter in letter_coords[1:]:
        goto(letter, drag=True)
        time.sleep(0.02)
    
    pyautogui.mouseUp()

board = input("Enter board: ").upper()
words = solver.solve(board)
time.sleep(3)

for word_coords, word in words:
    print(word)
    do_word(word_coords)
    time.sleep(0.05)

