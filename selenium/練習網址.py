from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from selenium.webdriver.chrome.options import Options #設定的物件
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

#設定 Chrome Driver 的執行檔路徑
options =Options()
options.chrome_executable_path="C:\\Users\HsiehHa\Desktop\Selenium 函式庫\selenium\chromedriver.exe"



#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化

driver.get("https://example.oxxostudio.tw/python/selenium/demo.html")
time.sleep(5)


select = Select(driver.find_element(By.ID, 'select'))
select.select_by_index(2)

time.sleep(2)