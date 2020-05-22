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

def words():
    
        list = []
        Swords = []
        final = []
        res = []
        final2 = []
        res2 = []

        driver = webdriver.Firefox(executable_path=geckopath)
        driver.get('https://www.hackthissite.org/')
        
        Login = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[1]/input'))
        )
        Login.send_keys('login')
        
        Pw = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[2]/input'))
        )
        Pw.send_keys('Password')

        Button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="innerlogin"]/p[3]/input'))
        )
        Button.click()    
        
        driver.get('https://www.hackthissite.org/missions/prog/1/')
        for i in range(1,11):
            Addwords = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[5]/td[2]/table/tbody/tr['+str(i)+']/td[2]/li')
            txt = Addwords.text
            for perm in permutations(txt, len(txt)):
                perm = ''.join(perm)
                Swords.append(perm)
        with open("wordlist.txt" ,'r') as wordlist:
            for rows in wordlist:
                for r in range(len(Swords)):
                    if Swords[r] == rows.strip("\n"):
                        final.append(Swords[r])
                        [res.append(x) for x in final if x not in res]
                       

        
        for r in range(len(Swords)):
            if Swords[r] in res:
                final2.append(Swords[r])
                [res2.append(x) for x in final2 if x not in res2] 
        print(f"{res2[0]},{res2[1]},{res2[2]},{res2[3]},{res2[4]},{res2[5]},{res2[6]},{res2[7]},{res2[8]},{res2[9]}")
       
        

words()
