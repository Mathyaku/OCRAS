# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 19:47:28 2018

@author: Matheus
"""
from OCR import ocr
from WebCrawling import reference_services
from bottle import route, run, template, request
import time
import json

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/img/extractText', 'POST')
def index():
    print("oi")
    init = time.time()   
    data = request.body.read()
    data = json.loads(data.decode())
    img_name = data.get('name', None)
    path = 'C:/Users/Matheus/Downloads/'
    print(img_name)
    print(path)
    result = ocr.imgToText(path+img_name, path, 'pt-br')
    print(result)
    
    if(img_name == None):
        return {'status': 'failed', 'result':'', 'time': time.time() - init}
    else:
        return {'status': 'sucess', 'result': '', 'time': time.time() - init}

@route('/img/extractReferences', 'POST')
def index():
    init = time.time()  
    
    print('olars')
    
    data = request.body.read()
    data = json.loads(data.decode())
    text = data.get('text', None)
    lang = data.get('lang', 'english')
    
    print('olars2')
        
    if(text == None):
        return {'status': 'failed', 'result':'', 'time': time.time() - init}
    else:
        return {'status': 'sucess', 'result': reference_services.get_results(text, language = lang ), 'time': time.time() - init}


run(host='localhost', port=8888)

