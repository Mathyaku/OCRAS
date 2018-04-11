# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:48:19 2018

@author: Raissa
"""

import requests
import json
from bs4 import BeautifulSoup

# SETUP

def findGoogleScholarReferences(key = "test",nPages = 2, file = "googleAcademicOutput.json"):
    extractedReferences = []
    
    for page in range(nPages):
        url = "https://scholar.google.com.br/scholar?start="+ str(page*10) +"&q="+ key.replace(" ", "+") +"&hl=pt-BR&as_sdt=0,5"
        page = requests.get(url)
        
        if(page.status_code != 200):
            return(dict([("references", []),("connection", 'failed')]))
                
        soup = BeautifulSoup(page.content, 'html.parser')
        expectedReferences = soup.find_all('div', class_='gs_r gs_or gs_scl')
        
        for reference in expectedReferences:
            soup2 = BeautifulSoup(str(reference), 'html.parser')
            try:
                a = soup2.find('h3', class_='gs_rt')
                title = a.find('a').get_text()
                url = a.find('a', href=True)['href']
                author = soup2.find('div', class_='gs_a').get_text()
                description = soup2.find('div', class_='gs_rs').get_text()
                extractedReferences.append(dict([("title", title),("url", url),("author", author),("description", description)]))
            except:
                #print('error')
                pass
            
    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "googleScholar"), ("connection", 'success')]))

def findScieloReferences(key = "test", nPages = 2, file = "scieloOutput.json"):
    extractedReferences = []
    
    for page in range(nPages):
        
        url = "https://search.scielo.org/?q="+ key.replace(" ", "+") +"&lang=en&count=10&from="+ str( (10*page)+1 )+"&output=site&sort=&format=summary&fb=&page=" + str(page+1) + "&where=&filter%5Bla%5D%5B%5D=pt&filter%5Bla%5D%5B%5D=en"
        page = requests.get(url)
        
        if(page.status_code != 200):
            return(dict([("references", []),("connection", 'failed')]))
                
        soup = BeautifulSoup(page.content, 'html.parser')
        expectedReferences = soup.find_all('div', class_='item')
        
        for reference in expectedReferences:
            soup2 = BeautifulSoup(str(reference), 'html.parser')
            try:
                a = soup2.find('div', class_='line')
                title = soup2.find('strong', class_='title').get_text()
                url = a.find('a', href=True)['href']
                author = soup2.find('div', class_='line authors').get_text().replace("\n", "")
                extractedReferences.append(dict([("title", title),("url", url),("author", author),("description", findScieloDescription(url))]))
            except:
                #print('error')
                pass
            
    storeInJson(extractedReferences, file)
    return(dict([("references", extractedReferences),("source", "scielo"), ("connection", 'success')]))
 
def findScieloDescription(url):
    page = requests.get(url)
    if(page.status_code != 200):
        return("")
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        description = soup.find_all('div', class_='abstract')[0].get_text()
        return(description.replace("\n", ""))
        
    
def findLinkSpringerReferences(key = "test",nPages = 2, file = "linkSpringerOutput.json"):
    extractedReferences = []
    nPages = 2
    file = "linkSpringerOutput.json"
    for page in range(nPages):
        url = "https://link-springer-com.ez27.periodicos.capes.gov.br/search/page/"+ str(page) +"?query="+ key.replace(" ", "+") 
        url = "https://link-springer-com.ez27.periodicos.capes.gov.br/search/page/1?query=multivariate+time+series+forecasting"
        
        page = requests.get(url)
        
        if(page.status_code != 200):
            return(dict([("references", []),("connection", 'failed')]))
                
        soup = BeautifulSoup(page.content, 'html.parser')
        expectedReferences = soup.find('ol').find_all('li')
        
        for reference in expectedReferences:
            try:
                title = reference.find('a', class_='title').get_text()
                url = reference.find('a', class_='title')['href']
                author = reference.find('span', class_='authors').get_text().replace('\n',' ').replace('  ','')
                description = reference.find('p', class_='snippet').get_text().replace('\n',' ').replace('  ','')
                extractedReferences.append(dict([("title", title),
                                                 ("url",  'https://link-springer-com.ez27.periodicos.capes.gov.br' + url),
                                                 ("author", author),
                                                 ("description", description)]))
            except:
                #print('error')
                pass
                        
    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "linkSpringer"),("connection", 'success')]))

#downloading and converting to JSON
def storeInJson(extractedReferences, file):
    with open(file, "w") as text_file:
        text_file.write(json.dumps(extractedReferences))

#opening the JSON
def getJsonReferences(file = "googleAcademicOutput.json"):
    return(json.load(open(file)))








#<h3 class="gs_rt" ontouchstart="gs_evt_dsp(event)">
#          <a data-clk="hl=pt-BR&amp;sa=T&amp;ct=res&amp;cd=7&amp;ei=bUnKWo3-FYiGmwH6jo3wAg&amp;scisig=AAGBfm24vwW-PhtCY-ynaVjVQNWXJs_qNQ&amp;nossl=1" href="http://psycnet.apa.org/record/1967-13475-001">