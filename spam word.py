import random
import pyautogui as pg
import time

parole = ("ciao", "buongiorno")
time.sleep(8)

for i in range(100):
    a = random.choice(parole)
    pg.write(a)
    pg.press("enter")