import numpy as np
import cv2
import keyboard
import pyautogui
import win32gui
import cv2
import time
from PyQt5.QtWidgets import QApplication
import sys
hwnd = win32gui.FindWindow(0, 'MixMaster Online')
res=1
def update_res():
  global res 
  res = 2
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
        time.sleep(0.01)
        pyautogui.press(position)
        time.sleep(0.01)
        pyautogui.press(heal_function)
        time.sleep(0.01)
        pyautogui.press('8')
        print("80%")
        
    elif hp==60:
        time.sleep(0.01)
        pyautogui.press(position)
        time.sleep(0.01)
        pyautogui.press(heal_function)
        time.sleep(0.01)
        pyautogui.press('8')
        print("50%")
    elif hp==40:
        time.sleep(0.01)
        pyautogui.press(position)
        time.sleep(0.01)
        pyautogui.press(heal_function)
        time.sleep(0.01) 
        pyautogui.press('8')
        print("50%")
    elif hp==40:
        time.sleep(0.01)
        pyautogui.press(position)
        time.sleep(0.01)
        pyautogui.press(heal_function)
        time.sleep(0.01)
        pyautogui.press('8')
        print("40%")
    elif hp==20:
        time.sleep(0.01)
        pyautogui.press(position)
        time.sleep(0.01)
        pyautogui.press(heal_function)
        time.sleep(0.01)
        pyautogui.press('8')
        print("30%")
    else:
        time.sleep(0.01)
        pyautogui.press('8')

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
while res==1:
    if keyboard.is_pressed('h'):
        while 1==1:
            generate_img()
            img = cv2.imread('output.png')
            role = [img[22, 758],img[33, 747],img[40, 746],img[55, 749],img[65, 753]]
            pet1 = [img[22, 823],img[33, 813],img[40, 813],img[55, 814],img[65, 819]]
            pet2 = [img[22, 888],img[33, 880],img[40, 878],img[55, 880],img[65, 888]]
            pet3 = [img[22, 952],img[33, 942],img[40, 943],img[55, 943],img[65, 951]]
            heal(calc_status(role),'1','f1')
            heal(calc_status(pet1),'2','f1')
            heal(calc_status(pet2),'3','f1')
            heal(calc_status(pet3),'4','f1')
    
# print(calc_status(role)) #[32, 31, 47]