# -*- coding: utf-8 -*-
"""
Created on Wed May  9 19:51:43 2018

@author: Matheus
"""

from rake_nltk import Rake

def GetRelevanteKeyWords(text, quantity, language):
    
    r = Rake(language=language)
    
    r.extract_keywords_from_text(text)
    
    r.get_ranked_phrases() # To get keyword phrases ranked highest to lowest.
    
    
    
    r.get_word_frequency_distribution()
    
    teste = r.get_word_degrees()
    
    
    
    keyWordsSorted = sorted(teste.items(), key=lambda x: x[1], reverse = True)
    
    keyWordsRelevante = [x[0] for x in keyWordsSorted[0:quantity]]
    
    return {'keywords': keyWordsRelevante, 'result': keyWordsSorted}



text = "cry The Project MATHEUS Matheus Gutenberg EBook of  a a a a a a cry matheus Crime and Punishment, cry by  MATHEUS Matheus Fyodor Dostoevsky\r\n"
keyWordsExtraction = GetRelevanteKeyWords(text, 5, "english")  # portuguese or english

keyWordsExtraction['keywords']
keyWordsExtraction['result']