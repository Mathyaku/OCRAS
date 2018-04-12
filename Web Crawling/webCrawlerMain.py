# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:21:37 2018

@author: Matheus
"""

import get_academic_sources as service
import extractContent as ec

<<<<<<< HEAD
extractedReferences = service.findLinkSpringerReferences("multivariate time series forecasting", 2)
all_1 = ec.get_content(extractedReferences['references'], extractedReferences['source'] )
=======
extractedReferences = service.findGoogleScholarReferences("multivariate time series forecasting", 2)

extractedReferences = service.findScieloReferences(key = "test", nPages = 2, file = "scieloOutput.json", language = "en")
>>>>>>> a0421cc25177d34a350d257475dcef92644ebf12
