# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:21:37 2018

@author: Matheus
"""

import get_academic_sources as service
import extractContent as ec

#extractedReferences = service.findGoogleScholarReferences("multivariate time series forecasting", 2)

extractedReferences = service.findScieloReferences(key = "test", nPages = 2, file = "scieloOutput.json", language = "en")