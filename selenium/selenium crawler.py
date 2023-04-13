from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from selenium.webdriver.chrome.options import Options #設定的物件

options =Options()
options.chrome_executable_path="C:\\Users\HsiehHa\Desktop\Selenium 函式庫\selenium\chromedriver.exe"

#建立 Driver 物件實體，用程式操作瀏覽器運作
driver =  webdriver.Chrome(options=options) 
driver.maximize_window() #視窗大化

#開啟網頁
driver.get("https://www.ptt.cc/bbs/movie/index.html")
# print(driver.page_source) #取得網頁的原始碼
#取得文章標題
#有可能不只一個element要+s
tags = driver.find_elements(By.CLASS_NAME, "title") #搜尋 class 屬性是 title 的所有標籤
# print(tags) #會印出python對網頁的程式碼

#迴圈抓取
for tag in tags:
    print(tag.text) #.text取得標籤的文字


#取得上一頁的文章標題

# link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
# link.click() #模擬使用者點擊上一頁
# tags = driver.find_elements(By.CLASS_NAME, "title")
# for tag in tags:
#     print(tag.text)


#用for迴圈 重複取得上一頁的文章標題
for i in range(2):  # 重複點擊 2 次
    try:
        link = driver.find_element(By.LINK_TEXT, "‹ 上頁")
        link.click()
        tags = driver.find_elements(By.CLASS_NAME, "title")
        for tag in tags:
            print(tag.text)
    except:
        # 找不到上一頁的連結或到達第一頁，退出迴圈
        break
driver.close()