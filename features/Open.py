import os
import keyboard
import pyautogui
import webbrowser
from time import sleep

def OpenExe(Query):
    Query = str(Query).lower()

    if "visit" in Query:
        Nameofweb =Query.replace("visit%","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True
    
    elif "open" in Query:
        nameoftheapp = Query.replace("open", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True

    elif "start" in Query:
        nameoftheapp = Query.replace("open", "")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True