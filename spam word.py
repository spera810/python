import random
import pyautogui as pg
import time

parole = ("hello", "hi")
time.sleep(10)

for i in range(100):
    a = random.choice(parole)
    pg.write(a)
    pg.press("enter")
