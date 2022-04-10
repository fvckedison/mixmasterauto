import numpy as np
import cv2
import keyboard
import pyautogui
import win32gui
import cv2
from PyQt5.QtWidgets import QApplication
import sys
hwnd = win32gui.FindWindow(0, 'MixMaster Online')

pet=[0,0,0,0,0,0]
back=[0,0,0,0,0,0]
def get_position():
    global pet
    if (keyboard.is_pressed('l')):
        pet[0]=pyautogui.position()[0]
        pet[1]=pyautogui.position()[1]
    elif (keyboard.is_pressed(';')):
        pet[2]=pyautogui.position()[0]
        pet[3]=pyautogui.position()[1]
    elif (keyboard.is_pressed(']')):
        pet[4]=pyautogui.position()[0]
        pet[5]=pyautogui.position()[1]
    elif (keyboard.is_pressed(',')):
        back[0]=pyautogui.position()[0]
        back[1]=pyautogui.position()[1]
    elif (keyboard.is_pressed('.')):
        back[2]=pyautogui.position()[0]
        back[3]=pyautogui.position()[1]
    elif (keyboard.is_pressed('/')):
        back[4]=pyautogui.position()[0]
        back[5]=pyautogui.position()[1]        
def convertQImageToMat(incomingImage):
    incomingImage = incomingImage.convertToFormat(4)
    width = incomingImage.width()
    height = incomingImage.height()
    ptr = incomingImage.bits()
    ptr.setsize(incomingImage.byteCount())
    arr = np.array(ptr).reshape(height, width, 4)  # Copies the data
    return arr

def heal(hp,position,heal_function):
    if hp==80:
        pyautogui.keyDown(position)
        pyautogui.keyUp(position)
        pyautogui.keyDown(heal_function)
        pyautogui.keyUp(heal_function)
        pyautogui.keyDown('8')
        pyautogui.keyUp('8')
        print("80%")
        
    elif hp==60:
        pyautogui.keyDown(position)
        pyautogui.keyUp(position)
        pyautogui.keyDown(heal_function)
        pyautogui.keyUp(heal_function)
        pyautogui.keyDown('8')
        pyautogui.keyUp('8')
        print("50%")
    elif hp==40:
        if(position==1):
            pyautogui.keyDown(position)
            pyautogui.keyUp(position)
            pyautogui.keyDown(heal_function)
            pyautogui.keyUp(heal_function)
            pyautogui.keyDown('8')
            pyautogui.keyUp('8')
        # else:
        #     if(position==2):
        #         pyautogui.keyDown('h')
        #         pyautogui.keyUp('h')
        #         pyautogui.moveTo(pet[0], pet[1],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')
        #     elif(position==3):
        #         pyautogui.keyDown('h')
        #         pyautogui.keyUp('h')
        #         pyautogui.moveTo(pet[2], pet[3],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')
        #     elif(position==4):
        #         pyautogui.keyDown('h')
        #         pyautogui.keyUp('h')
        #         pyautogui.moveTo(pet[4], pet[5],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')  
    elif hp==20:
        if(position==1):
            pyautogui.keyDown(position)
            pyautogui.keyUp(position)
            pyautogui.keyDown(heal_function)
            pyautogui.keyUp(heal_function)
            pyautogui.keyDown('8')
            pyautogui.keyUp('8')
        # else:
        #     if(position==2):
        #         pyautogui.moveTo(pet[0], pet[1],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')
        #     elif(position==3):
        #         pyautogui.moveTo(pet[2], pet[3],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')
        #     elif(position==4):
        #         pyautogui.moveTo(pet[4], pet[5],0.1)
        #         pyautogui.click(clicks=2, interval=0.5, button='left')
        print("30%")
    else:
        pyautogui.keyDown('8')
        pyautogui.keyUp('8')

def calc_status(dataSet):
    data=np.array(dataSet)
    print(data)
    for i in range(5):
        if(data[i][1])!=0:
            return (100-(i+1)*20)

def generate_img():
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    data = screen.grabWindow(hwnd).toImage()
    print(screen)
    data=convertQImageToMat(data)#將獲取的影象從QImage轉換為RBG格式
    cv2.imwrite('output.png', data)
def limit_skill():
    if keyboard.is_pressed('f1'): 
        if((pet[0]!=0 or pet[1]!=0) and (pet[2]!=0 or pet[3]!=0) and( pet[4]!=0 or pet[5]!=0)and (back[0]!=0 or back[1]!=0) and (back[2]!=0 or back[3]!=0) and( back[4]!=0 or back[5]!=0)):
            pyautogui.moveTo(back[0], back[1],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')
            pyautogui.moveTo(back[2], back[3],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')
            pyautogui.moveTo(back[4], back[5],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')
            pyautogui.moveTo(pet[0], pet[1],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')
            pyautogui.moveTo(pet[2], pet[3],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')
            pyautogui.moveTo(pet[4], pet[5],0.1)
            pyautogui.click(clicks=2, interval=0.5, button='left')

while True:
    generate_img()
    # get_position()
    # limit_skill()
    img = cv2.imread('output.png')
    role = [img[22, 758],img[33, 747],img[40, 746],img[55, 749],img[65, 753]]
    pet1 = [img[22, 823],img[33, 813],img[40, 813],img[55, 814],img[65, 819]]
    pet2 = [img[22, 888],img[33, 880],img[40, 878],img[55, 880],img[65, 888]]
    pet3 = [img[22, 952],img[33, 942],img[40, 943],img[55, 943],img[65, 951]]
    heal(calc_status(role),'1','f5')
    heal(calc_status(pet1),'2','f5')
    heal(calc_status(pet2),'3','f5')
    heal(calc_status(pet3),'4','f5')
    
# print(calc_status(role)) #[32, 31, 47]