from selenium import webdriver
from selenium.webdriver.common.by import By #引入selenium的By類別
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #鍵盤
import time
from selenium.webdriver.support.ui import WebDriverWait
import os
import glob

prefs = {'download.default_directory': os.path.abspath('file_download')} #指定到檔案相對路徑用os.path.abspath回給絕對路徑
options = webdriver.ChromeOptions()# 建立一個ChromeOptions物件options，用於設定Chrome瀏覽器的選項。
options.add_experimental_option('prefs', prefs) #：將剛剛建立的prefs字典加入到Chrome選項中，指定Chrome下載檔案時的預設下載路徑。

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://worker.stage.myviewboard.cloud/') #這是測試用網址
driver.maximize_window() #視窗大化

time.sleep(3)
options.add_experimental_option('prefs', prefs)
account = driver.find_element(By.XPATH,'//input[@placeholder="帳號"]')
account.send_keys('DCC')
password = driver.find_element(By.XPATH,'//input[@placeholder="密碼"]')
password.send_keys('DCC')
login = driver.find_element(By.XPATH,'//button[@type="button"]')
login.send_keys(Keys.ENTER)
time.sleep(6)

file_list = []

while True:
    all_elements = driver.find_elements(By.XPATH, '//td')
    download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]')

    for i in range(0, len(all_elements), 9):
        all_elements = driver.find_elements(By.XPATH, '//td')
        download_buttons = driver.find_elements(By.XPATH, '//a[text()="原檔"]')
        create_time = all_elements[i+1].text
        files_name = all_elements[i+3].text
        test1 = create_time.replace(':', '-')  # 處理字串
        new_file_name = test1 + ' '+ files_name
        print(f'下載 {new_file_name}')

        download_buttons[i//9].click()
        
        while os.path.isfile(f"./file_download/{files_name}") == False:
            time.sleep(1)
        # 修改檔名
        filename = glob.glob(os.path.join(os.path.abspath('file_download'), '*'))[0]
        os.rename(filename, os.path.join(os.path.abspath('file_download'), new_file_name))
        
        
        while os.path.isfile(f"./file_download/{new_file_name}") == False:
            time.sleep(1)
        print(os.listdir("./file_download")[0])

        for deletefile_download in os.listdir('file_download'):
            os.remove(os.path.join('file_download', deletefile_download))
            time.sleep(2)