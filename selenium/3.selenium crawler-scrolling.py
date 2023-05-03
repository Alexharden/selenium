from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from selenium.webdriver.chrome.options import Options #設定的物件

import time

#設定Chorme Drive 的執行檔路徑
options =Options()
options.chrome_executable_path="C:\\Users\HsiehHa\Desktop\Selenium 函式庫\selenium\chromedriver.exe"

#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化

#開啟網頁 
driver.get("https://www.104.com.tw/jobs/search/?ro=0&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=16&asc=0&page=3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1")
#捲動視窗並等待瀏覽器載入更多的內容 (java捲動視窗)
n = 0
while n < 3: #重複捲動三次
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#捲動視窗到底部
    time.sleep(3) #等待三秒
    n += 1

#取得網頁中工作的標題
titleTags = driver.find_elements(By.CLASS_NAME, "js-job-link")
for titleTag in titleTags:
    print(titleTag.text)  


driver.close()