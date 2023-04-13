#載入selenium相關模組
from selenium import webdriver
from selenium.webdriver.chrome.options import Options #設定的物件
#設定 Chrome Driver 的執行檔路徑
options =Options()
options.chrome_executable_path="C:\\Users\HsiehHa\Desktop\Selenium 函式庫\selenium\chromedriver.exe"

#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化

driver.get("https://www.google.com/") #開啟網頁
driver.save_screenshot("google.png") #網頁截圖
driver.get("https://www.youtube.com/")
driver.save_screenshot("youtube.png")

driver.close()