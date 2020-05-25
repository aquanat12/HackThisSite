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
    
        char = ''
        prime = 0
        nprime = 0
        
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
        
        driver.get('https://www.hackthissite.org/missions/prog/12/')
        
        
        info = driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/input').get_attribute("value")
        
        for i in range(len(info)):
            if info[i].isdigit() == True:
                if (int(info[i])) == 0 or (int(info[i])) == 1:
                    continue
                elif ((int(info[i]) == 2) or (int(info[i]) == 3)) or ((int(info[i]) == 5) or (int(info[i]) == 7)):
                    prime = prime + int(info[i])
                else:
                    nprime = nprime + int(info[i])
            else:
                new = chr((ord(info[i]) + 1))
                char = char + new
        total = prime * nprime
        char = char[0:25]
        ans = char + str(total)
        print (ans)
     #  print (prime)
     #  print (nprime)
     #  print (char)


        Sol = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/input'))
        )
        Sol.send_keys(ans)

        Submit = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr/td[2]/form/div/input'))
        )
        Submit.click()    
        

func()



def test():

        char = ''
        prime = 0
        nprime = 0

        info = 'xl2gr3y8x#read3zd1nbqsuap6jbl$sqr77pk37nm?g7z9cdtoyu8jnyaijvk5a4jkt2ek4g2xl??5cj$c#8jqirgesnaylas4gya12vij9qq?zhnbxwy5ckwa8o3l$1?ptupzzalx$@9bpe8f3a37k54i39ca43$vw$22khzr3nirotxeexiypvav29f@hltmp2r4qow@od75lynv3sy31akwsvkk$paqzih0usra87ddfeqcqqoqx32jjg$eh@#b3$9emt@5kg4kg@pslb3ua49??t8zi2a5p5xjkn8n8j$u6xzy@s#vo?n#gi19@u@qmfmlh#tncuqzd1et#l78?#@lf?94cutt@tpfqaoog1lletuob@rt93flt3u7i9rb75v?xx?fsvejn@c08v?@?wl#sghzmqho2gj8jv#xpx@6z2?i3yttlmszi3s6wpoicvb3gy6vsrond#f0i77ra?adzgtb34spsj7rqa#n50#o@gif9xr?qa4ixm$e2cyoe3uoq5i$6lx?6bio25xor750a1#k9cih3nxl0weu0bz5itjd#zn2p#jvo8u4?1r4?8y3r0dl2djlt19k1cht37smpm$ht82cn1@9a?fkt@ts593?$@1ygc5fcl7yj3'
        for i in range(len(info)):
            if info[i].isdigit() == True:
                if (int(info[i])) == 0 or (int(info[i])) == 1:
                    continue
                elif (int(info[i]) % 2 == 0) or (int(info[i]) % 3 == 0):
                    prime = prime + int(info[i])
                else:
                    nprime = nprime + int(info[i])
            elif info[i].isalpha():
                continue
            else:
                new = chr((ord(info[i]) + 1))
                char = char + new
        total = prime * nprime
        char = char[0:25]
        ans = char + str(total)
       # print (info)
        print (prime)
        print (nprime)
        print (char)
        
        
#test()
