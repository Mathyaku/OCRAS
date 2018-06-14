# -*- coding: utf-8 -*-

# Optical Character Recognition (OCR)

from PIL import Image 
import pytesseract 
import PythonMagick as pm
#import argparse
#import cv2
#import os
from OCR import deskew
from OCR import improvement
from OCR import binarisation

#
#
## Tratando imagem passada como parâmetro
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required=True,	help="path to input image file")
#ap.add_argument("-o", "--output", required=True, help="path to output image file")
#args = vars(ap.parse_args())
#
#


## por - portugues , eng - english
def imgToText(inputPath, outputPath, lang):
    # Localizando o modulo
    pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

    # Rotacionando imagem
    deskew.rotateImage(inputPath,outputPath)
    
    # Aumento da qualidade da imagem
    improvement.imageSharpness(outputPath)
    
    # Binarização e remoção de ruídos
    binarisation.noiseRemoval(outputPath)
    
    # Extraindo o texto da imagem'
    return( pytesseract.image_to_string(Image.open(outputPath), lang = lang)) 