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
                a = soup2.find_all('h3', class_='gs_rt')[0]
                title = a.find_all('a')[0].get_text()
                url = a.find_all('a', href=True)[0]['href']
                author = soup2.find_all('div', class_='gs_a')[0].get_text()
                description = soup2.find_all('div', class_='gs_rs')[0].get_text()
                extractedReferences.append(dict([("title", title),("url", url),("author", author),("description", description)]))
            except:
                #print('error')
                pass
            
    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "googleScholar"), ("connection", 'success')]))
    

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