from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from itertools import permutations
import time

geckopath = "./geckodriver.exe"

def func():
    
        list = ''

        driver = webdriver.Firefox(executable_path=geckopath)
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
        
        driver.get('https://www.hackthissite.org/missions/prog/11/')
        
        
        info = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]').text
        
        for i in range(len(info)):
            if i > 183:
                if info[i] == '\n':
                    continue
                elif info[i] == 'S':
                    continue
                elif info[i] == 'h':
                    continue    
                elif info[i] == 'i':
                    continue
                elif info[i] == 'f':
                    continue
                elif info[i] == 't':
                    continue
                elif info[i] == ':':
                    continue
                elif info[i] == 'D':
                    break
                list = list + info[i]
 
        split = list.split()
        string = split[0]
        shift = split[1]
        ans = ''
        for j in range(len(string)):
            if string[j].isdigit() == True and string[j+1].isdigit() == True and string[j+2].isdigit() == True:
                ans = ans + chr(int((string[j] + string[j+1] + string[j+2])) - int(shift))
            elif string[j].isdigit() == True and string[j+1].isdigit() == True and string[j+2].isdigit() == False:
                ans = ans + chr(int((string[j] + string[j+1])) - int(shift))
            else: 
                continue
          
        print (shift)
        print (string)
        print (ans)

        Sol = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/form/input'))
        )
        Sol.send_keys(ans)

        Submit = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[2]/form/div/input'))
        )
        Submit.click()    
        

func()
