# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 15:21:37 2018

@author: Matheus
"""

import get_academic_sources as service

extractedReferences = service.findGoogleScholarReferences("test eu", 2, "googleAcademicOutput.json")