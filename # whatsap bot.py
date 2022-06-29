import time
import pyautogui as pg
prompt = input("chizi ke minevise : ")
number = int(input("tedad bari ke oon chizo minevise (bad az zadane in dokme 10 sanie vaght dari beri to whatsap va ro jai ke payam ro vared mikoni click koni) : "))
def run_app(a, b):
    time.sleep(10)
    for i in range(b):
        pg.typewrite(a)
        pg.press("enter")
run_app(prompt, number)
# Easy