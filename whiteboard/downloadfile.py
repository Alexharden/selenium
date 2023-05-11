#-*- coding: utf-8 -*-
import pyautogui
import os, time
from PIL import Image

#開啟白板
os.popen('C:\\Program Files\\ViewSonic\\vBoard\\vBoard.exe')

time.sleep(10)


# 圖片下載路徑
magic_box = r'./image/magicbox.jpg' #百寶箱的圖
m_steel_channel = r'./image/m_steelchannel.jpg' #c槽
m_user_folder = r'./image/m_Users.jpg' #使用者資料夾
m_hsiehha_folder = r'./image/m_HsiehHa.jpg' #哈登資料夾
m_desktop_folder = r'./image/m_Desktop.jpg'#桌面資料夾
m_selenium_folder = r'./image/m_Seleniumfolder.jpg' 
m_file_download_folder = r'./image/m_filedownload.jpg' #下載資料夾
m_olf_image = r'./image/m_olfimage.jpg' #olf 檔案的圖
select_allpage = r'./image/selectallpage.jpg' #選取所有頁面
import_landscape = r'./image/importlandscape.jpg' #水平匯入檔案
page_menagement_menu = r'./image/pagemanagementmenu.jpg' #頁面管理
delete_page= r'./image/deletepage.jpg' #刪除頁面
confirm_delete = r'./image/confirmyes.jpg' #確認刪除 是


#存檔路徑
save_as_image = r'./image/saveas.jpg' #另存新檔
f_steel_channel = r'./image/f_steelchannel.jpg' #c槽
f_user_folder = r'./image/f_Users.jpg' #使用者資料夾
f_hsiehha_folder = r'./image/f_HsiehHa.jpg' #哈登資料夾
f_desktop_folder = r'./image/f_Desktop.jpg'#桌面資料夾
f_selenium_folder = r'./image/f_Seleniumfolder.jpg' 
f_converted_file_folder = r'./image/f_convertedfile.jpg' #轉檔資料夾
rename_olf_file = r'./image/rename_olffile.jpg' #重新命名




# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
mouse= pyautogui.locateCenterOnScreen(magic_box, confidence= 0.9) #百寶箱
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)


# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
mouse = pyautogui.locateCenterOnScreen(m_steel_channel, confidence= 0.9) #c槽
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_user_folder, confidence= 0.93) #使用者資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_hsiehha_folder, confidence= 0.9) #哈登資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_desktop_folder, confidence= 0.9) #桌面資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_selenium_folder, confidence= 0.88) #selenium資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_file_download_folder, confidence= 0.95) #測試資料夾
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(1)

mouse = pyautogui.locateCenterOnScreen(m_olf_image, confidence= 0.97) #olf圖案
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=2, interval=0.1, button='left')
time.sleep(3)

mouse= pyautogui.locateCenterOnScreen(select_allpage , confidence= 0.9) #選取所有頁面
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)

mouse= pyautogui.locateCenterOnScreen(import_landscape, confidence= 0.9) #水平匯入檔案
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)

mouse= pyautogui.locateCenterOnScreen(page_menagement_menu , confidence= 0.9) #頁面管理
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)

mouse= pyautogui.locateCenterOnScreen(delete_page, confidence= 0.9) #刪除頁面
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)


mouse= pyautogui.locateCenterOnScreen(confirm_delete, confidence= 0.9) #確認刪除 是
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)

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

mouse= pyautogui.locateCenterOnScreen(rename_olf_file, confidence= 0.9) #重新命名
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(1)
pyautogui.press('shiftleft')
time.sleep(1)
pyautogui.press('1')
time.sleep(3)
pyautogui.press('enter')
time.sleep(1)
#關閉白板 殺白板
os.system('TASKKILL /F /IM vBoard.exe /T')
time.sleep(10)
