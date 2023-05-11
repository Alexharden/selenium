import pyautogui
import os, time
from PIL import Image



save_as_image = r'./image/saveas.jpg' #另存新檔
f_steel_channel = r'./image/f_steelchannel.jpg' #c槽
f_user_folder = r'./image/f_Users.jpg' #使用者資料夾
f_hsiehha_folder = r'./image/f_HsiehHa.jpg' #哈登資料夾
f_desktop_folder = r'./image/f_Desktop.jpg'#桌面資料夾
f_selenium_folder = r'./image/f_Seleniumfolder.jpg' 
f_converted_file_folder = r'./image/f_convertedfile.jpg' #轉檔資料夾
rename_olf_file = r'./image/rename_olffile.jpg'


# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
os.popen('C:\\Program Files\\ViewSonic\\vBoard\\vBoard.exe')
time.sleep(12)
pyautogui.press('esc')
pyautogui.hotkey('ctrl', "1")
time.sleep(1)

mouse= pyautogui.locateCenterOnScreen(save_as_image, confidence= 0.9) #另存新檔
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)


mouse = pyautogui.locateCenterOnScreen(f_steel_channel, confidence= 0.9) #c槽
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(f_user_folder, confidence= 0.9) #使用者資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(f_hsiehha_folder, confidence= 0.9) #哈登資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(f_desktop_folder, confidence= 0.9) #桌面資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.1, button='left')
time.sleep(1)
mouse = pyautogui.locateCenterOnScreen(f_desktop_folder, confidence= 0.9) #桌面資料夾
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(f_selenium_folder, confidence= 0.9) #selenium資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)


mouse = pyautogui.locateCenterOnScreen(f_converted_file_folder, confidence= 0.9) #converted_file資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse= pyautogui.locateCenterOnScreen(rename_olf_file, confidence= 0.9) #重新命名
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)