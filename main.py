# coding: utf-8

import time

import keyboard
import numpy as np
import pyautogui
import pyscreenshot as ImageGrab

x, y, w, h = 824, 226, 758, 758

cells = 30
cell_size = w / cells

while True:
    if keyboard.is_pressed('q'):
        break
    im = ImageGrab.grab(bbox=(x, y, x + w, y + h))
    im = np.array(im)
    avg_color = np.array([
        [im[int(i * cell_size):int((i + 1) * cell_size), int(j * cell_size):int((j + 1) * cell_size), 1].mean(
            axis=(0, 1)) for j in range(cells)]
        for i in range(cells)
    ])

    m = np.min(avg_color)

    if m > 180:
        time.sleep(0.1)
        continue

    pos = np.unravel_index(np.argmin(avg_color), avg_color.shape)

    mx, my = int(x + (pos[1] + 0.5) * cell_size), int(y + (pos[0] + 0.5) * cell_size)

    pyautogui.moveTo(mx, my)
    pyautogui.click()
    time.sleep(0.03)
