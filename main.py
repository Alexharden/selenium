from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os, time, glob, shutil, pyperclip, pyautogui

from PIL import Image
#自動下載及安裝webdriver

prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

#建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#連線到 LeetCode登入頁面
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

driver.maximize_window() #視窗大化
# driver.implicitly_wait(40)
time.sleep(3)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(3)

#取得整個網頁的 建立時間和檔案名稱
create_time = driver.find_elements(By.XPATH,'//td')
files_name = driver.find_elements(By.XPATH,'//td')
test1 = create_time[1].text.replace(":", "-")  #處理字串 replace(填入被取代的值, 取代值)
new_filename = test1 + ' '+ files_name[3].text #組成新字串
print(new_filename) # 列印出來確認新字串的名稱

#搜尋網頁上的第一個原檔
download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]') [0]
dowload_file = download_buttons.click()
#WebDriverWait(driver,最大可以的時間) until 當條件成立時回傳True繼續往下執行 || lambda d: d會接受 len(內的結果當結果為True回傳到d)
WebDriverWait(driver, 120).until(lambda d: len(os.listdir('file_download')) > 0) 
time.sleep(10)
os.system('taskkill /F /IM chrome.exe') #關閉網頁 殺死網頁 抓完檔案

#將下載下來的檔案改名稱
#os.path.join(os.path.abspath) 組成完整路徑
#glob.glob 會回傳符合搜尋條件的檔案路徑，這裡使用 * 來代表所有檔案。
# [0] glob.glob 回傳的是一個列表，而我們只需要第一個符合搜尋條件的檔案，所以使用索引 [0] 取得第一個符合搜尋條件的檔案路徑。
filename = glob.glob(os.path.join(os.path.abspath('file_download'), '*'))[0]

#filename 是上一個函式 glob.glob 取得的檔案路徑。
#將檔案改名
os.rename(filename, os.path.join(os.path.abspath('file_download'), new_filename))
time.sleep(3)

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



#以下操作是自動化將檔案丟到w上再轉存成olf檔案的過程
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
time.sleep(5)

mouse= pyautogui.locateCenterOnScreen(select_allpage , confidence= 0.9) #選取所有頁面
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(3)

mouse= pyautogui.locateCenterOnScreen(import_landscape, confidence= 0.9) #水平匯入檔案
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(5)

mouse= pyautogui.locateCenterOnScreen(page_menagement_menu, confidence= 0.9) #水平匯入檔案
print(mouse)
time.sleep(1)
pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
time.sleep(1)
pyautogui.click(clicks=1, interval=0.5, button='left')
time.sleep(5)

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
time.sleep(2)
pyperclip.copy(new_filename) #複製名稱
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
time.sleep(2)
pyautogui.press('enter')
time.sleep(1)

#關閉白板 殺白板
os.system('TASKKILL /F /IM vBoard.exe /T')
time.sleep(10)

#切換回瀏覽器
# 取得目前開啟的所有瀏覽器窗口
windows = driver.window_handles

# 逐一判斷每個瀏覽器窗口是否符合標題
for window in windows:
    driver.switch_to.window(window)
    if "Myviewboard File Conversion" in driver.title:
        # 如果符合標題，就切換到這個瀏覽器窗口
        break

#上傳檔案
# 取得固定資料夾内唯一的檔案路徑
folder_path = 'C:\\Users\\HsiehHa\Desktop\\Selenium\\converted_file'
upload_file_folder = os.listdir(folder_path)[0]
file_path = os.path.join(folder_path, upload_file_folder)

#上傳檔案
upload_file = driver.find_elements(By.XPATH, '//input[@type="file"]')[0]
upload_file.send_keys(file_path)
time.sleep(10)


#刪除路徑資料夾內的所有檔案
for deletefile_download in os.listdir('file_download'):
    os.remove(os.path.join('file_download', deletefile_download))
time.sleep(2)

for deleteconverted_file in os.listdir('converted_file'):
    os.remove(os.path.join('converted_file', deleteconverted_file))
time.sleep(2)




time.sleep(1)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

driver.maximize_window() #視窗大化
# driver.implicitly_wait(40)
time.sleep(3)


#輸入帳號密碼 按下登入 批准帳號
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('admin')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('12345')
time.sleep(1)
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(3)

confirm_approve = driver.find_element(By.XPATH,'//p-radiobutton[@value="1"]')
confirm_approve.click()
time.sleep(3)