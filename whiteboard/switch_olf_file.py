#-*- coding: utf-8 -*-
import pyautogui
import os, time
from PIL import Image


#開啟白板
os.popen('C:\\Program Files\\ViewSonic\\vBoard\\vBoard.exe')
time.sleep(10)


# 圖片路徑
magic_box = r'./image/magicbox.jpg'
steel_channel = r'./image/steelchannel.jpg'
user_folder = r'./image/Users.jpg'
hsiehha_folder = r'./image/HsiehHa.jpg'
desktop_folder = r'./image/Desktop.jpg'
selenium_folder = r'./image/Seleniumfolder.jpg'
test_folder = r'./image/test.jpg'
olf_image = r'./image/olfimage.jpg'


# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
mouse= pyautogui.locateCenterOnScreen(magic_box, confidence= 0.8)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(3)


# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
mouse = pyautogui.locateCenterOnScreen(steel_channel, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(user_folder, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(hsiehha_folder, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(desktop_folder, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(selenium_folder, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(test_folder, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse = pyautogui.locateCenterOnScreen(olf_image, confidence= 0.76)
print(mouse)
pyautogui.moveTo(mouse, duration = 1.5) #用1.5秒移動到x=100，y=100的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

#關閉白板 殺白板
os.system('TASKKILL /F /IM vBoard.exe /T')
time.sleep(10)