# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:39:07 2023

@author: musta
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from selenium.common.exceptions import NoSuchElementException
import datetime
driver=webdriver.Chrome()
#driver.get("http://selenium.dev")
ticketUrl="https://www.passo.com.tr/tr/kategori/futbol-mac-biletleri/4615"
loginUrl="https://www.passo.com.tr/tr/giris"

ticketTeam='Galatasaray' #the team whose ticket will be bought

def login():#in start of the application some information is needed. Email, password and matchTime. Also security number will be asked too
    driver.get(loginUrl)
    email='eminer.2006@gmail.com'
    password='31cekeneren7A'
    number=input("Lütfen Güvenlik Anahtarını Giriniz!")
    matchTime='02:46'
   # loginBtn=driver.find_element(By.XPATH,'//i[@class="passo-icon passo-icon-user mr-1 small"]')
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    #loginBtn.click()
    time.sleep(2)
    userNameHolder=driver.find_element(By.XPATH,'//input[@type="text" and @autocomplete="username"]')
    passwordHolder=driver.find_element(By.XPATH,'//input[@type="password" and @autocomplete="current-password"]')
    securityHolder=driver.find_element(By.XPATH,'//input[@type="text" and @autocomplete="disabled"]')
    enterButton=driver.find_element(By.XPATH,'//button[@class="black-btn"]')
    userNameHolder.send_keys(email)
    passwordHolder.send_keys(password)
    securityHolder.send_keys(number)
    time.sleep(0.5)
    enterButton.click()
    
    
    
    
    
    
    

def findMatch():#fonction for determine the id of the match, and open the ticket page of the match
    #futbol= driver.find_element(By.XPATH,'//a[@class="nav-link text-dark" and @href="/tr/kategori/futbol-mac-biletleri/4615"]')
    #futbol.click()
    #driver.get(ticketUrl)
    time.sleep(0.5)
    allGames =driver.find_element(By.XPATH,'//div[@class="wrapper row event-search-items"]')
    innerhtml=allGames.get_attribute("innerHTML")
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all('div')]
    currentId=0
    for tag in all_tags:
        if tag.get('class') is not None and "col-md-4" in tag.get('class'):#looks for match list, matches seperated via col-md-4 tags
            currentId=tag.get('id')
        if ticketTeam in tag.text:
            break
    button = driver.find_element(By.ID, currentId)
    button.click()

        
    return currentId

def buyTicket():
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    purchaseBtn = driver.find_elements(By.XPATH,'//button[@class="red-btn"]')
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 400)")#scrolls the page for the button
    for btn in purchaseBtn:
        if btn.text=='SATIN AL':
            btn.click()
        else:
            continue
        
def selectCategory(flag):
    if flag:
        count=12
    else:
        count=13
    count=2
    while(True):
        xpath='//option[@value="{}: Object"]'.format(count)
        cat1= driver.find_element(By.XPATH,xpath)
        print(cat1.text)
        if 'Delux' in cat1.text or '8. Kategori' in cat1.text or '9. Kategori' in cat1.text:
            cat1.click()
            break
        else:
            continue
        
def discount():
    flag=True
    avaliable=False
    try:
        idInput= driver.find_element(By.XPATH,'//input[@type="text" and @placeholder="Lütfen TC Kimlik Numaranızı Giriniz."]')
        idInput.send_keys('17615315818')
    except NoSuchElementException:
        time.sleep(1.5)
        idInput= driver.find_element(By.XPATH,'//input[@type="text" and @placeholder="Lütfen TC Kimlik Numaranızı Giriniz."]')
        idInput.send_keys('17615315818')
        pass
    enterButton=driver.find_element(By.XPATH,'//button[@class="btn btn-primary btn-lg"]')
    enterButton.click()
    time.sleep(0.5)
    okayBtn=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
    okayBtn.click()
    time.sleep(1.5)
    selectCategory(flag)
    try:
        message = driver.find_element(By.XPATH,'//div[@id="swal2-content"]')
        if 'Bu kategori için uygun koltuk bulunamadı!' ==  message.text :
            okayBtn=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
            okayBtn.click()
            flag=False
            selectCategory(flag)
            try:
                secondMessage = driver.find_element(By.XPATH,'//div[@id="swal2-content"]')
                if 'Bu kategori için uygun koltuk bulunamadı!' ==  message.text :
                    okayBtn=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
                    okayBtn.click()
                    avaliable=False
            except NoSuchElementException:
                avaliable=True
                pass
        
    except NoSuchElementException:
        avalaible=True
        pass
    return avalaible
def ticketCount(count):
    time.sleep(0.75)
    selections=driver.find_elements(By.XPATH,'//select[@class="form-control"]/option')
    counter=0
    if count > len(selections):
        count=1   
    for tag in selections:
        if counter==count:
            tag.click()
            break
        counter+=1
def blockCount():
    flag=False
    while(not flag):
        blocks= driver.find_elements(By.XPATH,'//select[@id="blocks"]/option[@value!="0: null"]')
        for block in blocks:
            print(block.text)
            block.click()
            time.sleep(1)
            findSeat= driver.find_element(By.XPATH,'//button[@id="best_available_button"]')
            findSeat.click()
            time.sleep(1)
            try:
                confirmText=driver.find_element(By.XPATH,'//div[@class="text-secondary"]/span')
                print('sucess')
                flag=True
                break
            except NoSuchElementException:
                blocks= driver.find_elements(By.XPATH,'//select[@id="blocks"]/option[@value!="0: null"]')
                pass
def matchTimer(matchTime):
    now = datetime.datetime.now() 
    current_time = now.strftime('%H:%M:%S')
    curr=now.strftime('%H:%M')
    if curr== matchTime:
        time.sleep(2)
    while curr != matchTime:
        time.sleep(0.40)
        now = datetime.datetime.now() 
        current_time = now.strftime('%H:%M:%S')
        curr=now.strftime('%H:%M')
        if (int(matchTime[0:2])< int(now.strftime('%H'))) or  ((int(matchTime[0:2]) == int(now.strftime('%H'))) and (int(matchTime[3:5]) < int(now.strftime('%M')))):
            break
    

login()
matchTimer(matchTime)
time.sleep(1)
btn=driver.find_element(By.XPATH,'//a[@href="/tr/kategori/futbol-mac-biletleri/4615"]')
btn.click()
time.sleep(1)
findMatch()
time.sleep(1)
buyTicket()
time.sleep(0.50)
isTicketFound= discount()
ticketCount(1)
blockCount()

now = datetime.datetime.now() 
print(now)



     

