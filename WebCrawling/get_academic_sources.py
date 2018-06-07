# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:48:19 2018

@author: Raissa
"""

import requests
import json
from bs4 import BeautifulSoup
#import urllib2
import httplib2

# SETUP
def findGoogleScholarReferences(key = "test",nPages = 2, file = "googleAcademicOutput.json", language = "portuguese"):
    extractedReferences = []
    
    dict_languages = {'portuguese': 'pt-br', 'english': 'en-us'}
    for page in range(nPages):
        url = "https://scholar.google.com.br/scholar?start="+ str(page*10) +"&q="+ key.replace(" ", "+") +"&hl=" \
        + dict_languages.get(language) + "&as_sdt=0,5"
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
                extractedReferences.append(dict([("source", "google scholar"),("title", title),("url", url),("author", author),("description", description)]))
            except:
                #print('error')
                pass
            
#    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "google scholar"), ("connection", 'success')]))


# language can be 'pt' or 'en'
def findScieloReferences(key = "test", nPages = 2, file = "scieloOutput.json", language = "portuguese"):
    dict_languages = {'portuguese': 'pt', 'english': 'en'}
    extractedReferences = []
    
    
    for page in range(nPages):
        url = "https://search.scielo.org/?q="+ key.replace(" ", "+") +"&lang=en&count=10&from="+ str( (10*page)+1 )+ \
              "&output=site&sort=&format=summary&fb=&page=" + str(page+1) + "&where=&filter%5Bla%5D%5B%5D=" + \
              dict_languages.get(language, 'pt')
        page = requests.get(url)
        
        if(page.status_code != 200):
            return(dict([("references", []),("connection", 'failed')]))
                
        soup = BeautifulSoup(page.content, 'html.parser')
        expectedReferences = soup.find_all('div', class_='item')
            
        
        for reference in expectedReferences:
            soup2 = BeautifulSoup(str(reference), 'html.parser')
            refId = soup2.find('div', class_='item').get("id")
            
            #print("Id: {}".format(refId))
            try:
                a = soup2.find('div', class_='line')
                title = soup2.find('strong', class_='title').get_text()
                url = a.find('a', href=True)['href']
                author = soup2.find('div', class_='line authors').get_text().replace("\n", "")
                id_1 = refId+"_"+dict_languages.get(language, 'pt')
                
                
                description = soup2.find('div', {"id": id_1}).get_text().replace("\n", "")
                extractedReferences.append(dict([("source", "scielo"),("title", title),("url", url),("author", author),("description", description)]))
            except:
                print('error')
                pass
            
#    storeInJson(extractedReferences, file)
    return(dict([("references", extractedReferences),("source", "scielo"), ("connection", 'success')]))
        

def findLinkSpringerReferences(key = "test",nPages = 2, file = "linkSpringerOutput.json", language="pt"):
    extractedReferences = []
    for page in range(nPages):
        url = "https://link-springer-com.ez27.periodicos.capes.gov.br/search/page/"+ str(page) +"?query="+ key.replace(" ", "+") 
        #print(url)
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
                extractedReferences.append(dict([("source", "link springer"),("title", title),
                                                 ("url",  'https://link-springer-com.ez27.periodicos.capes.gov.br' + url),
                                                 ("author", author),
                                                 ("description", description)]))
            except:
                print('error')
                pass
                        
#    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "link springer"),("connection", 'success')]))



def findPubmed(key = "bird Health",nPages = 2, file = "pubmedOutput.json" , language="pt"):
    extractedReferences = []
    for page in range(nPages):
        url = "https://www.ncbi.nlm.nih.gov/pubmed/?term="+ str(page) +"?query="+ key.replace(" ", "+") 
        page = requests.get(url)

        if(page.status_code != 200):
            return(dict([("references", []),("connection", 'failed')]))
                
        soup = BeautifulSoup(page.content, 'html.parser')
        expectedReferences = soup.find_all('div', class_='rslt')
        
        for reference in expectedReferences:
#            try:
                title = reference.find('p', class_='title').get_text()
                print(reference.find('p', class_='title'))
                url = reference.find('p', class_='title')['href']
                author = reference.find('span', class_='desc').get_text().replace('\n',' ').replace('  ','')
                description = reference.find('p', class_='snippet').get_text().replace('\n',' ').replace('  ','')
#                extractedReferences.append(dict([("title", title),
#                                                 ("url",  'https://link-springer-com.ez27.periodicos.capes.gov.br' + url),
#                                                 ("author", author),
#                                                 ("description", description)]))
#            except:
#                print('error')
#                pass
                        
#    storeInJson(extractedReferences,file)
    return(dict([("references", extractedReferences),("source", "pubMed"),("connection", 'success')]))


#downloading and converting to JSON
def storeInJson(extractedReferences, file):
    with open(file, "w") as text_file:
        text_file.write(json.dumps(extractedReferences))

#opening the JSON
def getJsonReferences(file = "googleAcademicOutput.json"):
    return(json.load(open(file)))



import httplib2
def findAcademicMicrosoftReferences(key = "test",nPages = 2, file = "linkAcademicMicrosoft.json"):
    extractedReferences = []
    nPages = 2
    file = "linkAcademicMicrosoft.json"
    for page in range(nPages):
        url = "https://academic.microsoft.com/#/search?iq=%40"+ key.replace(" ", "%20") + "%40&q=" + key.replace(" ", "%20") + '&filters=&from=' + str((page-1)*8) +"&sort=0"
    #url = "https://academic.microsoft.com/#/search?iq=%40test%40&q=test&filters=&from=0&sort=0"
    
    h = httplib2.Http("/tmp/httplib2")
    resp, content = h.request(url)
    
    soup = BeautifulSoup(content, 'html.parser')
            
    page = requests.get(url)
    
    if(page.status_code != 200):
        #return(dict([("references", []),("connection", 'failed')]))
        pass
            
    soup = BeautifulSoup(page.content, 'html.parser')
    expectedReferences = soup.find_all('article')
        
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




#<h3 class="gs_rt" ontouchstart="gs_evt_dsp(event)">
#          <a data-clk="hl=pt-BR&amp;sa=T&amp;ct=res&amp;cd=7&amp;ei=bUnKWo3-FYiGmwH6jo3wAg&amp;scisig=AAGBfm24vwW-PhtCY-ynaVjVQNWXJs_qNQ&amp;nossl=1" href="http://psycnet.apa.org/record/1967-13475-001">