import pyautogui
import time
import keyboard
from ctypes import *
import threading
press=[0,0,0,0]
pet=[0,0,0,0,0,0]
pyautogui.FAILSAFE=False

    
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
        print(pyautogui.position())
        pet[0]=pyautogui.position()[0]
        pet[1]=pyautogui.position()[1]
    elif (keyboard.is_pressed(';')):
        print(pyautogui.position())
        pet[2]=pyautogui.position()[0]
        pet[3]=pyautogui.position()[1]
    elif (keyboard.is_pressed(']')):
        print(pyautogui.position())
        pet[4]=pyautogui.position()[0]
        pet[5]=pyautogui.position()[1]
    
def press_f2():
    
    while True:
        print(pet)
        if(pet[0]!=0 and pet[1]!=0 and pet[2]!=0 and pet[3]!=0 and pet[4]!=0 and pet[5]!=0 and press[0]!=0 and press[1]!=0 and press[2]!=0 and press[3]!=0):
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
            time.sleep(25)


def press_f7():
    while True:
        print(pet)
        if(pet[0]!=0 and pet[1]!=0 and pet[2]!=0 and pet[3]!=0 and pet[4]!=0 and pet[5]!=0 and press[0]!=0 and press[1]!=0 and press[2]!=0 and press[3]!=0):
            print(pet)
            pyautogui.keyDown('f4')
            pyautogui.keyUp('f4')
            pyautogui.moveTo(press[0], press[1],0.0)
            pyautogui.click(clicks=1, interval=0.0, button='left')
            windll.user32.BlockInput(True)
            pyautogui.moveTo(press[2], press[3],0.0)
            pyautogui.keyDown('8')
            pyautogui.keyUp('8')
            windll.user32.BlockInput(False)
            time.sleep(25)
            for i in range(0,5,2):
                print(i)
                pyautogui.keyDown('8')
                pyautogui.keyUp('8')
                pyautogui.moveTo(pet[i], pet[i+1],0)
                pyautogui.click(clicks=1, interval=0, button='left')
                windll.user32.BlockInput(True)
                pyautogui.moveTo(press[2], press[3],0.0)
                pyautogui.keyDown('8')
                pyautogui.keyUp('8')
                windll.user32.BlockInput(False)
                time.sleep(40)
            for i in range(0,29,1):
                pyautogui.keyDown('f4')
                pyautogui.keyUp('f4')
                pyautogui.moveTo(pet[0], pet[1],0.0)
                pyautogui.click(clicks=1, interval=0.0, button='left')
                windll.user32.BlockInput(True)
                pyautogui.moveTo(press[2], press[3],0.0)
                pyautogui.keyDown('8')
                pyautogui.keyUp('8')
                windll.user32.BlockInput(False)
                time.sleep(6)





if __name__ == "__main__":

    # t2 = threading.Thread(target = press_f2)
    # t2.setDaemon(True)
    # t2.start()

    # t4 = threading.Thread(target = press_f4)
    # t4.setDaemon(True)
    # t4.start()

    t7 = threading.Thread(target = press_f7)
    t7.setDaemon(True)
    t7.start()

    while True:
        pass
        get_position()
