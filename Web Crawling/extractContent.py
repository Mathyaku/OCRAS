# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:14:11 2018

@author: Raissa
"""

def get_content(refList = []):
    info = []
    for ref in refList:
        url = ref.get('url', None)
        if url.find('.pdf') > 0:
            ref['content'] = get_pdf_content(url)
        else:
            ref['content'] = get_site_content(url)
        info.append(ref)
    return info


def get_pdf_content(refList = []):
    page = requests.get(url)
        
    if(page.status_code != 200):
        return(dict([("content",[]),("status", 'failed')]))

    return(dict([("content", content),("status", 'failed')]))


