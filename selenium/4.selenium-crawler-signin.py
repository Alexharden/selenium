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
#連線到 LeetCode登入頁面 該網頁目前有防止機器人
driver.get("https://leetcode.com/accounts/login/")
#輸入帳號密碼 按下登入
usernameInput = driver.find_element(By.ID, "id_login") #帳號的位置
passwordInput = driver.find_element(By.ID, "id_password")#密碼的位置
signinBtn = driver.find_element(By.ID, "signin_btn") #登入按鈕的位置
usernameInput.send_keys("hardentest1") #輸入帳號
passwordInput.send_keys("hardentest0419")#輸入密碼
signinBtn.send_keys(Keys.ENTER)

time.sleep(10)
#等待登入完成
#連線到登入後才能取得資料的頁面，並取得想要的資料

driver.get("https://leetcode.com/problemest/all/")
time.sleep(5)
statElement = driver.find_element(By.CSS_SELECTOR, "[data-difficulty=TOTAL]" ) #根據任意欄位標籤
# print(statElement.text)
columns = statElement.text.split("\n") #放入列表
print("已完成刷題數量", columns[1])

driver.close()