import pyautogui
#判斷滑鼠位置

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot('whiteboard.jpg')
# print(im2)
# 圖片路徑
whileborad_image = r"./image/whiteboard.jpg"

# 跳用PyAutoGUI中的locateCenterOnscreen()函數 confidence 是圖片清晰度
whileborad_location = pyautogui.locateCenterOnScreen(whileborad_image, confidence= 0.6)
print(whileborad_location)
pyautogui.moveTo(whileborad_location, duration = 1.5) #用1.5秒移動到x=100，y=100的位置

print(pyautogui.position())