import pyautogui
import time
import keyboard
from ctypes import *
import threading
press=[0,0,0,0]
pet=[0,0,0,0,0,0]

def get_position():
    global press 
    global pet
    if keyboard.is_pressed('f10'):  
        press[0]=pyautogui.position()[0]
        press[1]=pyautogui.position()[1]
    elif (keyboard.is_pressed('f12')):
        press[2]=pyautogui.position()[0]
        press[3]=pyautogui.position()[1]
    elif (keyboard.is_pressed('l')):
        pet[0]=pyautogui.position()[0]
        pet[1]=pyautogui.position()[1]
    elif (keyboard.is_pressed(';')):
        pet[2]=pyautogui.position()[0]
        pet[3]=pyautogui.position()[1]
    elif (keyboard.is_pressed(']')):
        pet[4]=pyautogui.position()[0]
        pet[5]=pyautogui.position()[1]
    
def press_f2():
    
    while True:
        print(press)
        if(press[0]!=0 and press[1]!=0 and press[2]!=0 and press[3]!=0):
            windll.user32.BlockInput(True)
            pyautogui.keyDown('f2')
            pyautogui.keyUp('f2')
            pyautogui.moveTo(press[0], press[1],0.0)
            pyautogui.click(clicks=1, interval=0.0, button='left')
            
            pyautogui.moveTo(press[2], press[3],0.0)
            pyautogui.keyDown('8')
            pyautogui.keyUp('8')
            windll.user32.BlockInput(False)
            time.sleep(5)

def press_f4():
    while True:
        print('gg')
        if(press[0]!=0 and press[1]!=0 and press[2]!=0 and press[3]!=0):
            pyautogui.keyDown('f4')
            pyautogui.keyUp('f4')
            pyautogui.moveTo(press[0], press[1],0.0)
            pyautogui.click(clicks=1, interval=0.0, button='left')
            windll.user32.BlockInput(True)
            pyautogui.moveTo(press[2], press[3],0.0)
            pyautogui.keyDown('8')
            pyautogui.keyUp('8')
            windll.user32.BlockInput(False)
            time.sleep(100)


def press_f7():
    while True:
            if((pet[0]!=0 or pet[1]!=0) and (pet[2]!=0 or pet[3]!=0) and( pet[4]!=0 or pet[5]!=0)):
                for i in range(0,5,2):
                    pyautogui.keyDown('f7')
                    pyautogui.keyUp('f7')
                    pyautogui.moveTo(pet[i], pet[i+1],0.1)
                    pyautogui.click(clicks=1, interval=0.5, button='left') 
                    time.sleep(40)


if __name__ == "__main__":

    t2 = threading.Thread(target = press_f2)
    t2.setDaemon(True)
    t2.start()

    t4 = threading.Thread(target = press_f4)
    t4.setDaemon(True)
    t4.start()
    while True:
        pass
        get_position()
