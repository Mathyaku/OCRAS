# -*- coding: utf-8 -*-
"""
Created on Wed May  9 19:51:43 2018

@author: Matheus
"""

from rake_nltk import Rake

# função para ranquear as palavras do texto
def GetRelevanteKeyWords(text, quantity, language):
    
    r = Rake(language=language)
    
    r.extract_keywords_from_text(text)
    
    r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
    
    r.get_word_frequency_distribution()
    
    teste = r.get_word_degrees()
    
    
    
    keyWordsSorted = sorted(teste.items(), key=lambda x: x[1], reverse = True)
    
    keyWordsRelevante = [x[0] for x in keyWordsSorted[0:quantity]]
    
    return {'keywords': keyWordsRelevante, 'result': keyWordsSorted}


from nltk import WordNetLemmatizer
from nltk import re

# função para extrair os tokens do texto
def tokenize(str):

    # remove punctuation
    tokens = re.findall(r"<a.*?/a>|<[^\>]*>|[\w'@#]+",
        str.lower())

    # lemmatize words. try both noun and verb lemmatizations
    lmtzr = WordNetLemmatizer()
    for i in range(0,len(tokens)):
        res = lmtzr.lemmatize(tokens[i])
        if res == tokens[i]:
            tokens[i] = lmtzr.lemmatize(tokens[i], 'v')
        else:
            tokens[i] = res
    return tokens


text = "cry The Project MATHEUS Matheus Gutenberg EBook of  a a a a a a cry matheus Crime and Punishment, cry by  MATHEUS Matheus Fyodor Dostoevsky\r\n"


tokenize(text)


keyWordsExtraction = GetRelevanteKeyWords(text, 5, "english")  # portuguese or english

keyWordsExtraction['keywords']
keyWordsExtraction['result']