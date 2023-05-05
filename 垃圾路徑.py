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

prefs = {'download.default_directory': os.path.abspath('test')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

#建立一個Chrome瀏覽器的WebDriver物件driver，並傳入ChromeDriverManager().install()的值作為ChromeDriver的路徑，以及上面設定好的選項options。
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

#連線到 LeetCode登入頁面
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址

driver.maximize_window() #視窗大化
# driver.implicitly_wait(40)
time.sleep(3)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(3)


create_time = driver.find_elements(By.XPATH,'//td')
files_name = driver.find_elements(By.XPATH,'//td')
test1 = create_time[1].text.replace(":", "-")  #處理字串
test2 = test1 + ' '+ files_name[3].text
print(test2)

# for i in range(0, len(create_time), 9):
#     test1 = create_time[i+1].text.replace(":", "-")  #處理字串
#     print(test1 + ' ' + files_name[i + 3].text)



download_button = driver.find_elements(By.XPATH, '//a[text()="原檔"]') [0]
dowload_file = download_button.click()
time.sleep(3)

# for download_button in download_buttons:
#     download_button.click()
#     WebDriverWait(driver, 120).until(lambda d: len(os.listdir('test')) > 0)


