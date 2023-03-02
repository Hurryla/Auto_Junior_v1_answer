from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException    
import time
from PIL import Image
import io

#set url
site_locate = 'https://www.cathaybk.com.tw/cathaybk/'
url = site_locate
#set chrome
chrome_options = webdriver.ChromeOptions()


chrome_options.add_argument("--window-size=375,667")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--headless")
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--disable-dev-shm-usage')
# chrome_options.add_argument('--no-sandbox')

chrome_options.add_argument("user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1")

driver = webdriver.Chrome(options=chrome_options)

driver.get(url)
delay = 5 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.CSS_SELECTOR, "h2")))
    print ("Page is ready!")
except TimeoutException:
    print ("Loading took too much time!")

time.sleep(2)
driver.get_screenshot_as_file('截圖_開啟網頁.png')
image = Image.open('截圖_開啟網頁.png')
width, height = image.size
region = image.resize((width//2, height//2))
region.save('截圖_開啟網頁.png', 'PNG', optimize=True, quality=90)

#點擊選單
button = f'/html/body/div[1]/header/div/div[1]'
button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
action=ActionChains(driver)
action.move_to_element_with_offset(button, 5, 5)  # 0, 0 specifies no offset       
action.click().perform()

#點擊產品介紹
button = f'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div'
button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
action=ActionChains(driver)
action.move_to_element_with_offset(button, 5, 5)  # 0, 0 specifies no offset       
action.click().perform()

#點擊信用卡
button = f'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div'
button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
action=ActionChains(driver)
action.move_to_element_with_offset(button, 5, 5)  # 0, 0 specifies no offset       
action.click().perform()
time.sleep(2)

#計算 信用卡列表項目數量
elements = f'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]'
elements = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, elements))).text
number = len(elements.split('\n'))-1
print(f'用卡列表項目 數量：{number}')
driver.get_screenshot_as_file('截圖_信用卡列表.png')
image = Image.open('截圖_信用卡列表.png')
width, height = image.size
region = image.resize((width//2, height//2))
region.save('截圖_信用卡列表.png', 'PNG', optimize=True, quality=90)

#點擊卡片介紹
button = f'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div'
button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
action=ActionChains(driver)
action.move_to_element_with_offset(button, 5, 5)  # 0, 0 specifies no offset       
action.click().perform()

#計算 停發信用卡數量
button = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]'
button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
action=ActionChains(driver)
action.move_to_element_with_offset(button, 5, 5)  # 0, 0 specifies no offset   
action.perform()

elements = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]'
elements = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, elements)))
elements = elements.get_attribute('outerHTML')
number = elements.count("/span")
# print(elements)
print(f'停發信用卡 數量：{number}')

for i in range(number):
    cnt =i+1
    button = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[2]/span[{cnt}]'
    button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))
    action=ActionChains(driver)
    action.move_to_element_with_offset(button, 3, 3)  # 0, 0 specifies no offset       
    action.click().perform()
    time.sleep(2)

    button = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[{cnt}]/div/div[2]'
    button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))

    driver.get_screenshot_as_file(f'截圖_停發信用卡_{cnt}.png')
    image = Image.open(f'截圖_停發信用卡_{cnt}.png')
    width, height = image.size
    region = image.resize((width//2, height//2))
    region.save(f'截圖_停發信用卡_{cnt}.png', 'PNG', optimize=True, quality=90)
    print(f"截圖_停發信用卡_{cnt}.png done")
    




print("all done")

time.sleep(100000)


