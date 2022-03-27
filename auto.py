import pyautogui
import time
import keyboard
import time
from threading import Timer
press=[0,0]
pet=[0,0,0,0,0,0]

def get_position():
    global press 
    global pet
    if keyboard.is_pressed('f10'):  
        press=[pyautogui.position()[0],pyautogui.position()[1]]
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
    pyautogui.keyDown('f2')
    pyautogui.keyUp('f2')
    pyautogui.moveTo(press[0], press[1],0.1)
    pyautogui.click(clicks=1, interval=0.5, button='left')
    time.sleep(5)

def press_f4():
    pyautogui.keyDown('f4')
    pyautogui.keyUp('f4')
    pyautogui.moveTo(press[0], press[1],0.1)
    pyautogui.click(clicks=1, interval=0.5, button='left') 
    time.sleep(5)

def press_f7():
    for i in range(0,5,2):
        pyautogui.keyDown('f7')
        pyautogui.keyUp('f7')
        pyautogui.moveTo(pet[i], pet[i+1],0.1)
        pyautogui.click(clicks=1, interval=0.5, button='left') 
    


    time.sleep(5)

while True:
    get_position()
    
    if(press[0]!=0 or press[1]!=0):
        press_f2()
        press_f4()
    if((pet[0]!=0 or pet[1]!=0) and (pet[2]!=0 or pet[3]!=0) and( pet[4]!=0 or pet[5]!=0)):
        press_f7()

