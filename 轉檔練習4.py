from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
from selenium.webdriver.support.ui import WebDriverWait
import os
import time
import glob

#自動下載及安裝webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
download_defult = os.path.abspath('C://Users//HsiehHa//Desktop//路徑測試')	
prefs = {'download.default_directory': download_defult}
options.add_experimental_option('prefs', prefs)

#連線到 LeetCode登入頁面
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

driver.maximize_window() #視窗大化
# driver.implicitly_wait(40)
time.sleep(6)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(6)

# download = 
# filename = 'Y2 ST Animals and Living Things in  their habitat 2022 -23 1st half.flipchart'
# file_path = os.path.join(download, filename)



download_files = driver.find_elements(By.XPATH, '//a[text()="原檔"]')


for i in range(len(download_files)):
    download_files[i].click()
    time.sleep(60)
    # filename = 'Y2 ST Animals and Living Things in  their habitat 2022 -23 1st half.flipchart'  # 將filename設為下載的檔案名稱
    # file_path = os.path.join(download_path, filename)
    # while not os.path.exists(file_path):
    #     time.sleep(1)
    # print('檔案下載完成')

    
# start_time = time.time()
# while not os.path.exists(file_path):
#     time.sleep(1)
# 等待檔案下載







driver.quit()