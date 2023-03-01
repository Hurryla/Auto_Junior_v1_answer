import json
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
import datetime
import os
import random
import subprocess
from selenium.common.exceptions import TimeoutException

import time
# from stem import Signal
# from stem.control import Controller
import random
import io
from datetime import datetime
import csv
from selenium.webdriver.common.keys import Keys
import re
from selenium import webdriver    
from selenium.webdriver.chrome.options import Options
import datetime
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

def scrollDownAllTheWay(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, 100*document.body.scrollHeight);")

        time.sleep(3)

        if "Load next page</button>" in driver.page_source:
            driver.find_element_by_css_selector('.myButton').click()

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        last_height = new_height
        
#program processing timer
start_duration = datetime.datetime.now()

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


driver.get_screenshot_as_file('截圖_開啟網頁.png')

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

#計算 信用卡列表項目數量
elements = f'/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]'
elements = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, elements))).text
number = len(elements.split('\n'))-1
print(f'用卡列表項目 數量：{number}')
driver.get_screenshot_as_file('截圖_信用卡列表.png')

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

    button = f'/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div[{cnt}]/div/div[2]'
    button = WebDriverWait(driver, 1800).until(EC.element_to_be_clickable((By.XPATH, button)))

    driver.get_screenshot_as_file(f'截圖_停發信用卡_{cnt}.png')
    print(f"截圖_停發信用卡_{cnt}.png done")




print("all done")

time.sleep(100000)


