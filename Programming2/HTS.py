from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import urllib.request
import time
from PIL import Image
import numpy as np
from selenium.webdriver.chrome.options import Options
import pyautogui
import os



profile = webdriver.FirefoxProfile()

profile.set_preference("browser.download.folderList", 2)

profile.set_preference("browser.download.manager.showWhenStarting", False)

profile.set_preference("browser.download.dir", r'Your DIR')

profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 
                    
def get_key(val): 
    for key, value in MORSE_CODE_DICT.items(): 
         if val == value: 
             return key 
             
def func():
        
        if os.path.exists("image.png"):
            os.remove("image.png")

        list = []
        message = ''
        decipher = ''

        driver = webdriver.Firefox(executable_path="geckodriver.exe", firefox_profile=profile)
        actionChains = ActionChains(driver)
        driver.get('https://www.hackthissite.org/')
        
        Login = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[1]/input'))
        )
        Login.send_keys('Login')
        
        Pw = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[2]/input'))
        )
        Pw.send_keys('Password')

        Button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[3]/input'))
        )
        Button.click()    
        
        driver.get('https://www.hackthissite.org/missions/prog/2/')
        
        DL = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/img'))
        )
        actionChains.context_click(DL).perform() 
        
        time.sleep(0.5)
        pyautogui.typewrite(['down','down','down','down','enter'])
        time.sleep(0.5)
        pyautogui.typewrite('image.png')
        time.sleep(0.5)
        pyautogui.press('enter')

        
        time.sleep(1)

        im = Image.open('image.png', 'r')
        
        pix_val = np.asarray(im)

        result = np.where(pix_val != 0)

        for i in range((len(result[1]))):
            if int(result[1][i]) < 10:
                string2 = str(0) + str(result[1][i])
                string = str(result[0][i]) + string2
            else:
                string = str(result[0][i]) + str(result[1][i])
            list.append(int(string))
        
        for t in range(len(list)):
            if t == 0:
                message = message + chr(list[0])
                continue
            
            next = list[t] - list[t-1]
            message = message + chr(next)
        
        result = message.split()
        for j in range(len(result)): 
            val = result[j]
            decipher += get_key(val)
            
        print(decipher)
        

func()

