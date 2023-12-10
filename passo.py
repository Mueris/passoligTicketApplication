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
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.options import Options
import datetime
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout=50

driver = webdriver.Chrome()
options = Options()
options.add_argument("--headless=new")
driver2=webdriver.Chrome(options=options)

def export_cookies(driver):
    with open("cookies.txt", "w") as fd:
        fd.write(str(driver.get_cookies()))

def import_cookies(driver):
    with open("cookies.txt", "r") as fd:
        for cookie in eval(fd.read()):
            driver.add_cookie(cookie)

def headless():
    driver2.get('https://www.passo.com.tr/tr/etkinlik/trendyol-super-lig-sivasspor-galatasaray-bggrup-yeni-dort-eylul-stadyumu-mac-bileti-passo/5800327')
    element = driver2.find_elements(By.CSS_SELECTOR,'.box')
    innerhtml=element[1].get_attribute("innerHTML")
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all('li')]
    for tag in all_tags:
        print(tag.text)
    
    
    
    
#driver.get("http://selenium.dev")
ticketUrl="https://www.passo.com.tr/tr/kategori/futbol-mac-biletleri/4615"
loginUrl="https://www.passo.com.tr/tr/giris"

ticketTeam='Galatasaray' #the team whose ticket will be bought
ticketType='Deplasman'
matchTime='20:24'


def wait_for_all_elements(driver,by, value, timeout):
    try:
        return WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_all_elements_located((by, value)))
    except TimeoutException:
        print("TimeoutException: Element with XPath '{}' not found within {} seconds.".format(value, timeout))
        return None
def wait_for_element(driver,by, value, timeout):
    try:
        return WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        print("TimeoutException: Element with XPath '{}' not found within {} seconds.".format(value, timeout))
        return None

def login():#in start of the application some information is needed. Email, password and matchTime. Also security number will be asked too
    driver.get(loginUrl)
    
    email='eminer.2006@gmail.com'
    password='31cekeneren7A'
    number=input("Lütfen Güvenlik Anahtarını Giriniz!")
    
   # loginBtn=driver.find_element(By.XPATH,'//i[@class="passo-icon passo-icon-user mr-1 small"]')
    driver.set_window_size(1024, 600)
    driver.maximize_window()
    #loginBtn.click()
    time.sleep(2)
    userNameHolder=driver.find_element(By.XPATH,'//input[@type="text" and @autocomplete="username"]')
    passwordHolder=driver.find_element(By.XPATH,'//input[@type="password" and @autocomplete="current-password"]')
    securityHolder=driver.find_element(By.XPATH,'//input[@type="text" and @autocomplete="disabled"]')
    enterButton=driver.find_element(By.XPATH,'//button[@class="black-btn"]')
    
    try:
        driver.find_element(By.XPATH,'//a[@aria-label="dismiss cookie message"]').click()
    except NoSuchElementException:
        pass
    userNameHolder.send_keys(email)
    passwordHolder.send_keys(password)
    securityHolder.send_keys(number)
    time.sleep(0.5)
    enterButton.click()
    

def advirtasement():
    
    wait_for_element(driver,By.XPATH, '//a[@href="/tr/kategori/futbol-mac-biletleri/4615"]', 5)
    try:
        if driver.find_element(By.XPATH,'//button[@class="swal2-cancel swal2-styled"]').is_enabled():
            driver.find_element(By.XPATH,'//button[@class="swal2-cancel swal2-styled"]').click()
    except NoSuchElementException:
        print('noAdvertisement')
        pass
     
def allMatches():
    wait_for_element(driver,By.XPATH, '//div[@class="wrapper row event-search-items"]', timeout)
    allGames =driver.find_element(By.XPATH,'//div[@class="wrapper row event-search-items"]')
    innerhtml=allGames.get_attribute("innerHTML")
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all('div')]
    matches =[]
    for tag in all_tags:
        if tag.get('class') is not None and "col-md-4" in tag.get('class'):#looks for match list, matches seperated via col-md-4 tags
            currentId=tag.get('id')
            match = driver.find_element(By.XPATH,'//*[@id="{}"]/div[@class]/div[@class]/div[@class="row r-sub-description"]/div[@class]/div[@class]'.format(currentId))
            if 'Kombine' not in match.text and 'Yadigar' not in match.text:
                matches.append(match)
    return matches
    

def findMatch():#fonction for determine the id of the match, and open the ticket page of the match
    flag=False
    wait_for_element(driver,By.XPATH, '//div[@class="wrapper row event-search-items"]', timeout)
    timeoutFlag=False
    if timeoutFlag==False:
        allGames =driver.find_element(By.XPATH,'//div[@class="wrapper row event-search-items"]')
        innerhtml=allGames.get_attribute("innerHTML")
        dataSoup=BeautifulSoup(innerhtml,'html.parser')
        all_tags = [tag for tag in dataSoup.find_all('div')]
        currentId=0
        for tag in all_tags:
            if tag.get('class') is not None and "col-md-4" in tag.get('class'):#looks for match list, matches seperated via col-md-4 tags
                currentId=tag.get('id')
            if ticketTeam in tag.text:
                flag=True
                break
        if flag:
            button= wait_for_element(driver, By.ID, currentId, timeout)
            button.click()
            return currentId
        else:
            findMatch()
    else:
        findMatch()
    return currentId

def buyTicket():
    window_after = driver.window_handles[1]
    driver.switch_to.window(window_after)
    time.sleep(1.5)
    driver.execute_script("window.scrollTo(0, 400)")#scrolls the page for the button
    wait_for_element(driver,By.XPATH, '//button[@class="red-btn"]', timeout)
    #delay()
    try:
        wait_for_element(driver, By.XPATH,'//button[@class="red-btn"]',timeout)
        purchaseBtn = driver.find_elements(By.XPATH, '//button[@class="red-btn"]')
    except TimeoutException:
        driver.execute_script("window.scrollTo(0, 400)")#scrolls the page for the button
        wait_for_element(driver,By.XPATH, '//button[@class="red-btn"]', timeout)
        purchaseBtn = driver.find_elements(By.XPATH, '//button[@class="red-btn"]')
        
    for btn in purchaseBtn:
        if btn.text=='SATIN AL':
            btn.click()
        else:
            continue
        
def selectCategory(flag): 
    wait_for_element(driver, By.XPATH, '//div[@class="form-group ticket-type-group"]', timeout)
    choose= wait_for_all_elements(driver,By.XPATH, '//div[@class="col-12"]/select', timeout)
    innerhtml=choose[len(choose)-1].get_attribute("innerHTML")
    dataSoup=BeautifulSoup(innerhtml,'html.parser')
    all_tags = [tag for tag in dataSoup.find_all('option')]
    avaliable=False
    while(not avaliable):
        count=(len(all_tags)-2)-flag
        if ticketTeam=='Beşiktaş':
            count=(len(all_tags)-5)-flag
        xpath='//option[@value="{}: Object"]'.format(count)
        cat1= driver.find_element(By.XPATH,xpath)
        if ticketTeam=='Galatasaray' and ('Delux' in cat1.text or '8. Kategori' in cat1.text or '9. Kategori' in cat1.text or '7. Kategori' in cat1.text or '6. Kategori' in cat1.text) or ticketTeam!='Galatasaray' or ticketType=='Deplasman':
            cat1.click()
        elif ticketType=='Deplasman' and 'Misafir'.lower() in cat1.text.lower():
            cat1.click()
        else:
            flag+=1
            continue
        try:
            while(True):
                message= wait_for_element(driver, By.XPATH,'//div[@id="swal2-content"]', 2)
                if 'Bu kategori için uygun koltuk bulunamadı!' ==  message.text:
                    okayBtn=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
                    okayBtn.click()
                    flag+=1
                    break
        except (NoSuchElementException, AttributeError):
            avaliable=True
            pass
        
def discount():
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
    
def ticketCount(count):
    time.sleep(0.75)
    selections=wait_for_all_elements(driver, By.XPATH,'//select[@class="form-control"]/option', timeout)
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
        blocks= wait_for_all_elements(driver, By.XPATH,'//select[@id="blocks"]/option[@value!="0: null"]',timeout)
        for block in blocks:
            print(block.text)
            block.click()
            time.sleep(0.5)
            findSeat= wait_for_element(driver, By.XPATH, '//button[@id="best_available_button"]', timeout)
            findSeat.click()
            time.sleep(1)
            try:
                notAvaliable=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
                notAvaliable.click()
                continue
            except NoSuchElementException:
                pass
            try:
                confirmText=driver.find_element(By.XPATH,'//div[@class="text-secondary"]/span')
                print('sucess')
                flag=True
                return flag
            except NoSuchElementException:
                continue
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
def wait_for_element2(driver, value, timeout):
    try:
        now = datetime.datetime.now() 
        current_time = now.strftime('%H:%M:%S')
        print("before wait  {}".format(current_time))
        return WebDriverWait(driver, timeout, ignored_exceptions=(StaleElementReferenceException,)).until(EC.presence_of_element_located((By.XPATH, value)))
    except TimeoutException:
        print("TimeoutException: Element with XPath '{}' not found within {} seconds.".format(value, timeout))
        return None
    
def currTime(str):
   now = datetime.datetime.now() 
   current_time = now.strftime('%H:%M:%S')
   print(str,current_time)
    

login()
currTime('Baslangıc')
advirtasement()
currTime('Bitis')
matchTimer(matchTime)
currTime('Baslangıc')
btn= wait_for_element(driver,By.XPATH, '//a[@href="/tr/kategori/futbol-mac-biletleri/4615"]', timeout)
currTime('Bitis')
btn.click()
currTime('Baslangıc')
wait_for_element(driver,By.XPATH, '//div[@class="wrapper row event-search-items"]', timeout)
currTime('Bitis')
currTime('Baslangıc')
findMatch()
currTime('Bitis')
time.sleep(1)
currTime('Baslangıc')
wait_for_element(driver,By.XPATH, '//*[@class="passo-icon passo-icon-location"]', 10)#TAM BURDA HATA VAR NEDENSE BİR TÜRLÜ, HTMLİ ALGILAMIYOR EN KÖTÜ 3 5 SANİYE GAP VERİP GNDER
 #FİND MATCH İTERASYON YAPIYOR ACABA ONUN DA MI ZAMAN KISMI DÜZGÜN ÇALIŞIYOR ?
currTime('Bitis')
currTime('Baslangıc')
if ticketTeam=='Galatasaray':
    #discount()
    time.sleep(0.25)
currTime('Bitis')
try:
    buyTicket()
except ElementClickInterceptedException:
    driver.execute_script("window.scrollTo(0, 400)")#scrolls the page for the button
    buyTicket()
    pass
isTicketFound=False
while(not isTicketFound):
    try:#BURAYA EKLEDİM ÇIAKRIRSIN
        selectCategory(0)
    except IndexError:
        print('error')
        """""   
        btn=wait_for_element(driver,By.XPATH,'//a[@href="/tr/kategori/futbol-mac-biletleri/4615"]',timeout)
        btn.click()
        findMatch()
        buyTicket()
        """
        pass
    ticketCount(1)
    try:
        btn=driver.find_element(By.XPATH,'//button[@class="swal2-confirm swal2-styled"]')
        btn.click()
    except NoSuchElementException:
        pass
    isTicketFound=blockCount()
    
    now = datetime.datetime.now() 
    print(now)



     

