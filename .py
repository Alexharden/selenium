from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os, time, glob, shutil, pyperclip, pyautogui
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image

login_myviewboard = r'./image/login.jpg'#登入畫面
login_success = r'./image/login_success.jpg' #登入成功


prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

#建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
#連線到 LeetCode登入頁面

driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

driver.maximize_window() #視窗大化
# driver.implicitly_wait(40)
while pyautogui.locateCenterOnScreen(login_myviewboard, confidence= 0.9) == None:
    time.sleep(2)
print(f'成功進入到登入畫面囉 {login_myviewboard}')
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
driver.implicitly_wait(10)
# while pyautogui.locateCenterOnScreen(login_success, confidence= 0.9) == None:
#     time.sleep(1)
print(f'成功進入登入畫面 {login_success}')

    

isNextPage = True
currentPage = 1
while isNextPage:
    #登入圖片

    for i in range(0, 90, 9):
        # time.sleep(1)
        # prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
        # options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
        # options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

        # #建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
        # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        # WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, "'//button[@label]'")))
        WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//button[@label]')))
        state = driver.find_elements(By.XPATH, '//button[@label]')[i//9].text
        print(state)
        if  state != 'Review':
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//td')))
            all_elements = driver.find_elements(By.XPATH, '//td')
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//a[text()="原檔"]')))
        
            download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]') #下載按鈕的element
            create_time = all_elements[i+1].text #建立時間的element
            files_name = all_elements[i+3].text #檔案名稱的element
            test1 = create_time.replace(':', '-')  # 處理字串
            new_file_name = test1 + ' '+ files_name
            print(f'下載 {new_file_name}')

            download_buttons[i//9].click() #因為下載按鈕式獨立element 間距是9 i每重複執行一次會 +1
                
            while os.path.isfile(f'./file_download/{files_name}') == False: #動態檢查下載是否完成
                time.sleep(1)
            print('下載成功')
            driver.minimize_window() #視窗縮小
            print('縮小視窗')
            # 修改檔名
            filename = glob.glob(os.path.join(os.path.abspath('file_download'), '*'))[0]
            os.rename(filename, os.path.join(os.path.abspath('file_download'), new_file_name))
                
                
            while os.path.isfile(f'./file_download/{new_file_name}') == False: #動態檢查檔案是否改名完成
                time.sleep(1)
            print(os.listdir('./file_download')[0]) #單純用來看是不是真的有改名



            # 圖片下載路徑
            m_maintoolbar = r'./image/m_Main_ToolBar.jpg' #判斷w是否開啟的圖
            magic_box = r'./image/magicbox.jpg' #百寶箱的圖
            m_steel_channel = r'./image/m_steelchannel.jpg' #c槽
            m_user_folder = r'./image/m_Users.jpg' #使用者資料夾
            m_hsiehha_folder = r'./image/m_HsiehHa.jpg' #哈登資料夾
            m_desktop_folder = r'./image/m_Desktop.jpg'#桌面資料夾
            m_selenium_folder = r'./image/m_Seleniumfolder.jpg' 
            m_file_download_folder = r'./image/m_filedownload.jpg' #下載資料夾
            m_olf_image = r'./image/m_olfimage.jpg' #olf 檔案的圖
            select_allpage = r'./image/selectallpage.jpg' #選取所有頁面
            checkmark = r'./image/m_checkmark.jpg' #點所選取所有頁面 會打勾 來判斷是否點到了選取頁面    
            import_landscape = r'./image/importlandscape.jpg' #水平匯入檔案
            magic_tool = r'./image/m_magic_tool.jpg' #百寶箱的工具欄 來判斷是否匯入完成
            page_menagement_menu = r'./image/pagemanagementmenu.jpg' #頁面管理
            delete_page= r'./image/deletepage.jpg' #刪除頁面
            confirm_delete = r'./image/confirmyes.jpg' #確認刪除 是
            page1 = r'./image/page1.jpg' #判斷是否刪除掉空白第一頁
            
            #存檔路徑
            file_manager = r'./image/file_manager.jpg' #文件管理
            save_as_image = r'./image/saveas.jpg' #另存新檔
            f_steel_channel = r'./image/f_steelchannel.jpg' #c槽
            f_user_folder = r'./image/f_Users.jpg' #使用者資料夾
            f_hsiehha_folder = r'./image/f_HsiehHa.jpg' #哈登資料夾
            f_desktop_folder = r'./image/f_Desktop.jpg'#桌面資料夾
            f_selenium_folder = r'./image/f_Seleniumfolder.jpg' 
            f_converted_file_folder = r'./image/f_convertedfile.jpg' #轉檔資料夾
            rename_olf_file = r'./image/rename_olffile.jpg' #重新命名
            f_confirm_save = r'./image/f_confirm_save.jpg' #輸入檔案名稱後的 能不能點擊確認存檔的勾
            save_success = r'./image/save_success.jpg' #判斷 檔案是否存檔完成


            #開啟白板
            os.popen('C:\\Program Files\\ViewSonic\\vBoard\\vBoard.exe')
            while pyautogui.locateCenterOnScreen(m_maintoolbar, confidence= 0.9) == None:
                time.sleep(2)
            print(f'成功讀取到圖片 主選單 {m_maintoolbar}')


            #以下操作是自動化將檔案丟到w上再轉存成olf檔案的過程
            # 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
            mouse= pyautogui.locateCenterOnScreen(magic_box, confidence= 0.9) #百寶箱
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')

            while pyautogui.locateCenterOnScreen(m_steel_channel, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 c槽 {m_steel_channel}')


            # 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
            mouse = pyautogui.locateCenterOnScreen(m_steel_channel, confidence= 0.9) #c槽
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(m_user_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 使用者資料夾 {m_user_folder}')    

            mouse = pyautogui.locateCenterOnScreen(m_user_folder, confidence= 0.9) #使用者資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(m_hsiehha_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 harden資料夾 {m_hsiehha_folder}')       

            mouse = pyautogui.locateCenterOnScreen(m_hsiehha_folder, confidence= 0.9) #哈登資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')
            
            while pyautogui.locateCenterOnScreen(m_desktop_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 桌面資料夾 {m_desktop_folder}')

            mouse = pyautogui.locateCenterOnScreen(m_desktop_folder, confidence= 0.9) #桌面資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')
            
            while pyautogui.locateCenterOnScreen(m_selenium_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 selenium資料夾 {m_selenium_folder}')   
            
            mouse = pyautogui.locateCenterOnScreen(m_selenium_folder, confidence= 0.88) #selenium資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(m_file_download_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 下載資料夾 {m_file_download_folder}')    

            mouse = pyautogui.locateCenterOnScreen(m_file_download_folder, confidence= 0.9) #下載資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(m_olf_image, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 olf圖案 {m_olf_image}')   

            mouse = pyautogui.locateCenterOnScreen(m_olf_image, confidence= 0.9) #olf圖案
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')


            while pyautogui.locateCenterOnScreen(select_allpage, confidence= 0.9) == None:
                time.sleep(2)
            print(f'成功讀取到圖片 選取所有頁面 {select_allpage}')   

            mouse= pyautogui.locateCenterOnScreen(select_allpage , confidence= 0.9) #選取所有頁面
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')
            time.sleep(3)

            while pyautogui.locateCenterOnScreen(checkmark, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取 已選取所有頁面 {checkmark}')  

            mouse= pyautogui.locateCenterOnScreen(import_landscape, confidence= 0.9) #水平匯入檔案
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')
            time.sleep(5)

            while pyautogui.locateCenterOnScreen(magic_tool, confidence= 0.9) != None:
                time.sleep(3)
            print(f'成功匯入所有檔案  {magic_tool}')  

            mouse= pyautogui.locateCenterOnScreen(page_menagement_menu, confidence= 0.9) #頁面管理
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')

            while pyautogui.locateCenterOnScreen(delete_page, confidence= 0.9) == None:
                time.sleep(2)
            print(f'成功讀取到刪除頁面  {delete_page}')  

            mouse= pyautogui.locateCenterOnScreen(delete_page, confidence= 0.9) #刪除頁面
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')
            

            while pyautogui.locateCenterOnScreen(confirm_delete, confidence= 0.9) == None:
                time.sleep(2)
            print(f'成功讀取到 確認是否要刪除  {confirm_delete}')  

            mouse= pyautogui.locateCenterOnScreen(confirm_delete, confidence= 0.9) #確認刪除 是
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')

            while pyautogui.locateCenterOnScreen(page1, confidence= 0.9) == None:
                time.sleep(2)
            print(f'成功 將頁面刪除 並取讀取到第一頁  {page1}')  
            time.sleep(1)

            mouse = pyautogui.locateCenterOnScreen(file_manager, confidence= 0.9)
            print(mouse)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')

            # pyautogui.press('esc')  這是鍵盤操作的部分
            # pyautogui.hotkey('ctrl', "1")
            while pyautogui.locateCenterOnScreen(save_as_image, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 另存新檔  {save_as_image}')  

            mouse= pyautogui.locateCenterOnScreen(save_as_image, confidence= 0.9) #另存新檔
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')

            while pyautogui.locateCenterOnScreen(f_steel_channel, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 c槽 {f_steel_channel}')

            mouse = pyautogui.locateCenterOnScreen(f_steel_channel, confidence= 0.9) #c槽
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(f_user_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 使用者資料夾 {f_user_folder}')

            mouse = pyautogui.locateCenterOnScreen(f_user_folder, confidence= 0.9) #使用者資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(f_hsiehha_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 哈燈資料夾 {f_hsiehha_folder}')

            mouse = pyautogui.locateCenterOnScreen(f_hsiehha_folder, confidence= 0.9) #哈登資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(f_desktop_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 桌面資料夾 {f_desktop_folder}')

            mouse = pyautogui.locateCenterOnScreen(f_desktop_folder, confidence= 0.9) #桌面資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.1, button='left')
            time.sleep(1)
            #這邊到時候可以改掉 因為在電腦上他在底下點擊第一次會跑掉 所以在做第一次 雙擊
            mouse = pyautogui.locateCenterOnScreen(f_desktop_folder, confidence= 0.9) #桌面資料夾
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(f_selenium_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 selenium資料夾 {f_selenium_folder}')

            mouse = pyautogui.locateCenterOnScreen(f_selenium_folder, confidence= 0.9) #selenium資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')

            while pyautogui.locateCenterOnScreen(f_converted_file_folder, confidence= 0.9) == None:
                time.sleep(1)
            print(f'成功讀取到圖片 轉檔的資料夾 {f_converted_file_folder}')

            mouse = pyautogui.locateCenterOnScreen(f_converted_file_folder, confidence= 0.9) #converted_file資料夾
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=2, interval=0.1, button='left')
            time.sleep(1)
            print(f'成功讀取到 重新命名圖片{rename_olf_file}')

            mouse= pyautogui.locateCenterOnScreen(rename_olf_file, confidence= 0.9) #重新命名
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')
            time.sleep(2)
            print("點擊重新命名框")

            pyperclip.copy(new_file_name) #複製名稱
            time.sleep(1)
            print(f'複製名稱為 {new_file_name}')
            # paste_content = pyperclip.paste() #剪取剪貼簿的內容 這會有輸入法的問題
            # time.sleep(2)
            # pyautogui.typewrite(paste_content) # 貼上剪貼簿的內容 這會有輸入法的問題
            # time.sleep(2)
            pyautogui.hotkey('ctrl', 'v')  #鍵盤的操作 直接作複製貼上 就不會有輸入法的問題
            #pyautogui.press('enter')
            time.sleep(2)
            while pyautogui.locateCenterOnScreen(f_confirm_save, confidence= 0.9) == None:
                time.sleep(1)
            print(f'發現確認鈕 {f_confirm_save} 可以點擊確定 將檔案重新命名為 {new_file_name} ')
            mouse= pyautogui.locateCenterOnScreen(f_confirm_save, confidence= 0.9) #重新命名
            print(mouse)
            time.sleep(1)
            pyautogui.moveTo(mouse, duration = 0.1) #用0.1秒移動到座標 mouse 的位置
            time.sleep(1)
            pyautogui.click(clicks=1, interval=0.5, button='left')    

            while pyautogui.locateCenterOnScreen(save_success, confidence= 0.9) != None:
                time.sleep(1)

            print(f'確認檔案已經儲存完畢 可以執行關閉白板的動作 {save_success}')
            #關閉白板 殺白板
            os.system('TASKKILL /F /IM vBoard.exe /T')
            time.sleep(5)

            driver.maximize_window()
        
            # driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

            # #連線到 LeetCode登入頁面
            # driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

            # driver.maximize_window() #視窗大化
            # # driver.implicitly_wait(40)
            # while pyautogui.locateCenterOnScreen(login_myviewboard, confidence= 0.9) == None:
            #     time.sleep(2)
            # print(f'成功進入到登入畫面囉 {login_myviewboard}')
            # #輸入帳號密碼 按下登入
            # account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
            # account.send_keys('DCC')
            # password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
            # password.send_keys('DCC')
            # login = driver.find_element(By.XPATH,'//button[@type="button"]')
            # login.send_keys(Keys.ENTER)

            # while pyautogui.locateCenterOnScreen(login_success, confidence= 0.9) == None:
            #     time.sleep(1)
            # print(f'成功進入登入畫面 {login_success}')

            #上傳檔案
            # 取得固定資料夾内唯一的檔案路徑
            
            folder_path = 'C:\\Users\\HsiehHa\Desktop\\Selenium\\converted_file'
            upload_file_folder = os.listdir(folder_path)[0]
            file_path = os.path.join(folder_path, upload_file_folder)

            #上傳檔案
            WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, '//input[@type="file"]')))
            upload_file = driver.find_elements(By.XPATH, '//input[@type="file"]')[i//9] #按照順序往下上傳 跟著本來的迴圈
            upload_file.send_keys(file_path)
            while driver.find_elements(By.XPATH, '//button[@label]')[i//9].text != 'Review':
                time.sleep(1) #轉檔頁面上的檔案狀態
            
                # file_type = driver.find_elements(By.XPATH, '//button[@label="Progress"]')[i//9] #重新抓取元素，更新文字內容
            print('上傳成功囉')
            

            for deletefile_download in os.listdir('file_download'): #刪除檔案

                try:
                    os.remove(os.path.join('file_download', deletefile_download))
                except PermissionError:
                # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
                # 等待一段時間，讓其他程序釋放對檔案的使用權     
                    time.sleep(2)
                    os.remove(os.path.join('converted_file', deletefile_download))

            for deleteconverted_file in os.listdir('converted_file'):
                try:
                    os.remove(os.path.join('converted_file', deleteconverted_file))
                except PermissionError:
                # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
                # 等待一段時間，讓其他程序釋放對檔案的使用權            
                    time.sleep(2)
                    os.remove(os.path.join('converted_file', deleteconverted_file))
            print('檔案刪除完了')
            time.sleep(3)
        else:
            continue

    pageList = []
    WebDriverWait(driver, 10, 0.5).until(EC.presence_of_all_elements_located((By.XPATH, f'//a[@tabindex][text()]')))
    pageElements = driver.find_elements(By.XPATH, "//a[@tabindex][text()]")
    for i in range(len(pageElements)):
        pageList.append(pageElements[i].text)
    if str(currentPage + 1) in pageList:
        currentPage += 1
        WebDriverWait(driver, 10, 0.5).until(EC.element_to_be_clickable((By.XPATH, f'//a[@tabindex][text()="{str(currentPage)}"]')))
        driver.find_element(By.XPATH, f'//a[@tabindex][text()="{str(currentPage)}"]').click()
        print('點擊下一頁')

    else:
        isNextPage = False
        print('沒有下一頁了')

    