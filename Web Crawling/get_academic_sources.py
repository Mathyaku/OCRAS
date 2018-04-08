# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 13:48:19 2018

@author: Raissa
"""

import requests
url = "https://scholar.google.com.br/scholar?hl=pt-BR&as_sdt=0%2C5&q=test&btnG="
page = requests.get(url)
page.status_code
page.content
from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


[type(item) for item in list(soup.children)]
html = list(soup.children)[1]


list(html.children)[1]
len(list(html.children))
a = soup.find_all('h3', class_='gs_rt')[0]
title = a.find_all('a')[0].get_text()
url = a.find_all('a', href=True)[0]['href']



#<h3 class="gs_rt" ontouchstart="gs_evt_dsp(event)">
#          <a data-clk="hl=pt-BR&amp;sa=T&amp;ct=res&amp;cd=7&amp;ei=bUnKWo3-FYiGmwH6jo3wAg&amp;scisig=AAGBfm24vwW-PhtCY-ynaVjVQNWXJs_qNQ&amp;nossl=1" href="http://psycnet.apa.org/record/1967-13475-001">