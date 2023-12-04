# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 20:39:07 2023

@author: musta
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome()
driver.get("http://selenium.dev")
url="https://www.passo.com.tr/tr/kategori/futbol-mac-biletleri/4615"

ticketTeam='Kayserispor' #the team whose ticket will be bought
driver.get(url)

time.sleep(1)

def findGameId():#fonction for determine the id of the match, and open the ticket page of the match
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
findGameId()
        


