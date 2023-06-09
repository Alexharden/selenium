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


download = 'C:\\Users\\HsiehHa\\Downloads\\'
filename = 'Y2 ST Animals and Living Things in  their habitat 2022 -23 1st half.flipchart'
file_path = os.path.join(download, filename)



#尋找 "原檔" 存在列表中，下載第一個值，並按下點擊
download_files = driver.find_elements(By.XPATH, '//a[text()="原檔"]')[0]

download_files.click()

# 等待檔案下載
start_time = time.time()
while not os.path.exists(file_path):
    time.sleep(1)


#上傳檔案
upload_file = driver.find_elements(By.XPATH, '//input[@type="file"]')[0]
upload_file.send_keys('C:\\Users\\HsiehHa\\Downloads\\1.olf')
time.sleep(3)




driver.quit()