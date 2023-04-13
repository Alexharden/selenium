from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from selenium.webdriver.chrome.options import Options #設定的物件
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

options =Options()
options.chrome_executable_path ="C:\\Users\\HsiehHa\\Desktop\\Selenium 函式庫\\selenium\\chromedriver.exe"

#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化

#開啟網頁 
driver.get("https://www.104.com.tw/jobs/search/?ro=0&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=16&asc=0&page=3&mode=s&jobsource=2018indexpoc&langFlag=0&langStatus=0&recommendJob=1&hotJob=1")
#取得網頁中工作的標題
titleTags = driver.find_elements(By.CLASS_NAME, "js-job-link")
for titleTag in titleTags:
    # print(titleTag.text)  
    continue

select_page = Select(driver.find_element(By.ID, "js-sort"))
select_page.select_by_value("1-0")  
time.sleep(3)


#By.CLASS_NAME 只能用來找尋單一 class 名稱的元素，而這個元素有三個 class 名稱，
#分別為 page-select、js-paging-select、gtm-paging-top 
select_page1 = Select(driver.find_element(By.CSS_SELECTOR, ".page-select.js-paging-select.gtm-paging-top"))
time.sleep(3)
select_page1.select_by_value("2")  
time.sleep(3)

# element = driver.find_element(By.LINK_TEXT, "數位廣告行銷人員")
# element.click()
# time.sleep(10)
driver.quit()