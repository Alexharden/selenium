from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from selenium.webdriver.chrome.options import Options #設定的物件
import time
from selenium.webdriver.common.keys import Keys #鍵盤
#設定Chorme Drive 的執行檔路徑
options =Options()
options.chrome_executable_path="C:\\Users\HsiehHa\Desktop\Selenium 函式庫\selenium\chromedriver.exe"

#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化
#連線到 LeetCode登入頁面
driver.get("https://worker.myviewboard.cloud/")
driver.implicitly_wait(20)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,"//input[@placeholder='帳號']")
account.send_keys("admin")
password = driver.find_element(By.XPATH,"//input[@placeholder='密碼']")
password.send_keys("12345")


time.sleep(10)
driver.close()