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

timeout=180

driver = webdriver.Chrome()
options = Options()
options.add_argument("--headless=new")
driver2=webdriver.Chrome(options=options)



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
ticketType='Ev'
#matchTime=input(" MAÇ SAATİNİ SAAT:DAKİKA FORMATINDA YAZINIZI; ÖRNEK: 17:20 \n")
matchTime="02:49"


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
def run():
    driver.get(loginUrl)
def login():#in start of the application some information is needed. Email, password and matchTime. Also security number will be asked too

    email='eminer.2006@gmail.com'
    password='31cekeneren7A'
    """""
    email=input("Kullanıcı emaili: ")
    password=input("Şifrenizi Giriniz: ")
    """
    number=input("Lütfen Açılan Sitedeki Güvenlik Anahtarını Giriniz!")
    
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
        
        if wait_for_element(driver, By.XPATH, '//button[@class="swal2-cancel swal2-styled"]', 5) is not None:
            wait_for_element(driver, By.XPATH, '//button[@class="swal2-cancel swal2-styled"]', 5).click()
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
        pass
        
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
        count=(len(all_tags)-1)-flag
        if ticketTeam=='Beşiktaş':
            count=(len(all_tags)-5)-flag
        xpath='//option[@value="{}: Object"]'.format(count)
        cat1= wait_for_element(driver, By.XPATH, xpath, timeout)
        if ticketTeam=='Galatasaray' and ('8. Kategori' in cat1.text or '9. Kategori' in cat1.text or '7. Kategori' in cat1.text or '6. Kategori' in cat1.text):
            cat1.click()
        elif ticketType=='Deplasman' and 'MİSAFİR' in cat1.text:
            cat1.click()
        elif (ticketTeam=='Fenerbahçe' and ticketType=='Ev') and not('MİSAFİR' in cat1.text):
            cat1.click()
        else:
            flag+=1
            continue
        try:
            while(True):
                time.sleep(0.25)
                message= wait_for_element(driver, By.XPATH,'//div[@id="swal2-content"]', 2)
                if 'Bu kategori için uygun koltuk bulunamadı!' ==  message.text:
                    okayBtn=wait_for_element(driver, By.XPATH, '//button[@class="swal2-confirm swal2-styled"]', 3)
                    okayBtn.click()
                    flag+=1
                    break
        except (NoSuchElementException, AttributeError):
            avaliable=True
            pass
        
def loyalityCard():
    flag=False
    try:
        idInput= wait_for_element(driver,By.XPATH,'//input[@type="text" and @placeholder="Lütfen TC Kimlik Numaranızı Giriniz."]', 5)
        if idInput is not None:
            idInput.send_keys('17615315818')
            flag=True
    except NoSuchElementException:
        time.sleep(1.5)
        idInput= wait_for_element(driver,By.XPATH,'//input[@type="text" and @placeholder="Lütfen TC Kimlik Numaranızı Giriniz."]', 3)
        if idInput is not None:
            idInput.send_keys('17615315818')
            flag=True
        pass
    if flag:
        enterButton=wait_for_element(driver,By.XPATH,'//button[@class="btn btn-primary btn-lg"]',3)
        enterButton.click()
        time.sleep(0.5)
        okayBtn=wait_for_element(driver,By.XPATH,'//button[@class="swal2-confirm swal2-styled"]',3)
        okayBtn.click()
        time.sleep(1.5)
    
def ticketCount(count):
    selections=wait_for_all_elements(driver, By.XPATH,'//select[@class="form-control"]/option', timeout)
    counter=0#
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
            try:
                notAvaliable=wait_for_element(driver,By.XPATH,'//button[@class="swal2-confirm swal2-styled"]',2)
                if notAvaliable is not None:
                    notAvaliable.click()
                    continue
            except NoSuchElementException:
                pass
            try:
                confirmText=wait_for_element(driver,By.XPATH,'//div[@class="text-secondary"]/span',0.1)
                print('BAŞARILI')
                flag=True
                return flag
            except NoSuchElementException:
                continue
                pass
        
def matchTimer(matchTime2):
    now = datetime.datetime.now() 
    current_time = now.strftime('%H:%M:%S')
    curr=now.strftime('%H:%M')
    if curr== matchTime:
        time.sleep(1)
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
    
def runProgram(matchTime2):
    advirtasement()
    matchTimer(matchTime2)
    btn= wait_for_element(driver,By.XPATH, '//a[@href="/tr/kategori/futbol-mac-biletleri/4615"]', timeout)
    btn.click()
    wait_for_element(driver,By.XPATH, '//div[@class="wrapper row event-search-items"]', timeout)
    time.sleep(1)
    findMatch()
    time.sleep(1)
    wait_for_element(driver,By.XPATH, '//*[@class="passo-icon passo-icon-location"]', 10)#TAM BURDA HATA VAR NEDENSE BİR TÜRLÜ, HTMLİ ALGILAMIYOR EN KÖTÜ 3 5 SANİYE GAP VERİP GNDER
     #FİND MATCH İTERASYON YAPIYOR ACABA ONUN DA MI ZAMAN KISMI DÜZGÜN ÇALIŞIYOR ?
    try:
        buyTicket()
    except ElementClickInterceptedException:
        driver.execute_script("window.scrollTo(0, 400)")#scrolls the page for the button
        buyTicket()
        pass
    if ticketTeam=='Galatasaray':
        loyalityCard()
        time.sleep(0.25)
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



run()
login()
runProgram(matchTime)

