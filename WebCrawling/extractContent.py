# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:14:11 2018

@author: Raissa
"""
import requests
import json
from bs4 import BeautifulSoup

def get_content(refList = [], source="linkSpringer"):
    info = []
    for ref in refList:
        url = ref.get('url', None)
        if url.find('.pdf') > 0:
            ref['content'] = get_pdf_content(url)
        else:
            ref['content'] = get_site_content(url, source)
        info.append(ref)
    return info


def get_pdf_content(url = '' ):
    content = '' 
    page = requests.get(url)
        
    if(page.status_code != 200):
        return(dict([("content",'' ),("status", 'failed')]))

    return(dict([("content", content),("status", 'success')]))


def get_site_content(url = '', source="linkSpringer"):
    source="linkSpringer"
    url = 'https://link-springer-com.ez27.periodicos.capes.gov.br/chapter/10.1007/978-3-642-57678-2_63'
    content = '' 
    page = requests.get(url)
        
    if(page.status_code != 200):
        return(dict([("content",''),("status", 'failed')]))
    
    soup = BeautifulSoup(page.content, 'html.parser')
    if(source == "linkSpringer"):
        try:
            content = soup.find('section', class_='Abstract').get_text().replace('Abstract', '')
        except:
            pass
    
        return(dict([("content", content),("status", 'success')]))
