from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
import time
from selenium.webdriver.support.ui import WebDriverWait
import os
import glob


# for i in range(0, 90, 9):
prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址
driver.maximize_window() #視窗大化

time.sleep(3)
options.add_experimental_option('prefs', prefs)
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(6)

# download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]')
# all_elements = driver.find_elements(By.XPATH, '//td')
# download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]') #下載按鈕的element
# create_time = all_elements[i+1].text #建立時間的element
# files_name = all_elements[i+3].text #檔案名稱的element
# test1 = create_time.replace(':', '-')  # 處理字串
# new_file_name = test1 + ' '+ files_name
# download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]')
# download_buttons[i//9].click()
time.sleep(3)
# all_elements = driver.find_elements(By.XPATH, '//td')
currentPage = 1
pageList = []
pageElements = driver.find_elements(By.XPATH, "//a[@tabindex][text()]")
flag = True
while flag:
    for i in range(len(pageElements)):
        pageList.append(int(pageElements[i].text))

    if currentPage < len(pageElements) and currentPage in pageList:
        next_page = driver.find_element(By.XPATH, '//span[@class="ui-paginator-icon pi pi-caret-right"]')
        next_page.click()
        currentPage += 1
        pageList = []
        time.sleep(3)
    else:
        flag = False 
        break

driver.close()
# for i in range(len(pageElements)):
#     pageList.append(pageElements[i])

 
# if currentPage in pageList:
#     # driver.find_element(By.XPATH, f'//a[@tabindex][text()="{str(currentPage)}"]').click()
#     next_page.click()
# time.sleep(2)
# currentPage += 1   
# 在條件語句外面遞增 currentPage 變數

        

    # while os.path.isfile(f'./file_download/{files_name}') == False: #動態檢查下載是否完成
    #     time.sleep(1)
    # print('下載成功')    
    # #上傳檔案
    # # 取得固定資料夾内唯一的檔案路徑
    # folder_path = 'C:\\Users\\HsiehHa\Desktop\\Selenium\\converted_file'
    # upload_file_folder = os.listdir(folder_path)[0]
    # file_path = os.path.join(folder_path, upload_file_folder)

    # #上傳檔案
    # upload_file = driver.find_elements(By.XPATH, '//input[@type="file"]')[0]
    # upload_file.send_keys(file_path)
    # file_type = driver.find_elements(By.XPATH, f'//td=[@style="width: 5%"[@test()="已轉檔"]')[i//9] #轉檔頁面上的檔案狀態
    # print(file_type.text) 
    # while file_type.text != '已轉檔':
    #     time.sleep(2)
    #     # file_type = driver.find_elements(By.XPATH, '//button[@label="Progress"]')[i//9] #重新抓取元素，更新文字內容
    # print(f"{file_type.text}")
    # print("上傳成功囉")
       
    # time.sleep(10)



    # for deletefile_download in os.listdir('file_download'): #刪除檔案

    #     try:
    #         os.remove(os.path.join('file_download', deletefile_download))
    #     except PermissionError:
    #     # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
    #     # 等待一段時間，讓其他程序釋放對檔案的使用權     
    #         time.sleep(2)
    #         os.remove(os.path.join('converted_file', deletefile_download))

    # for deleteconverted_file in os.listdir('converted_file'):
    #     try:
    #         os.remove(os.path.join('converted_file', deleteconverted_file))
    #     except PermissionError:
    #     # 如果刪除失敗，可能是因為檔案正在被其他程序使用中
    #     # 等待一段時間，讓其他程序釋放對檔案的使用權            
    #         time.sleep(2)
    #         os.remove(os.path.join('converted_file', deleteconverted_file))

#     file_type = driver.find_elements(By.XPATH, '//button[@label="Review"]') 
# print(len(file_type))
