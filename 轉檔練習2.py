from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
from selenium.webdriver.support.select import Select   # 使用 Select 對應下拉選單
import time

#自動下載及安裝webdriver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window() #視窗大化
#連線到 LeetCode登入頁面
driver.get("https://worker.stage.myviewboard.cloud/")
# driver.implicitly_wait(40)
time.sleep(6)
#輸入帳號密碼 按下登入
account = driver.find_element(By.XPATH,"//input[@placeholder='帳號']")
account.send_keys("DCC")
password = driver.find_element(By.XPATH,"//input[@placeholder='密碼']")
password.send_keys("DCC")
login = driver.find_element(By.CLASS_NAME,"btn.btn-primary.px-4")
login.send_keys(Keys.ENTER)
#等待登入完成
time.sleep(10)
select_type = Select(driver.find_element(By.XPATH,'//select'))
select_type.select_by_value("New")

# download_files = driver.find_elements(By.LINK_TEXT, "原檔")
# download_files = driver.find_elements(By.XPATH, "//a[text()='原檔']")
# download_files.click(download_files[0])
time.sleep(5)
# driver.close()
