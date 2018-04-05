# -*- coding: utf-8 -*-

# Optical Character Recognition (OCR)

from PIL import Image 
import pytesseract 
import PythonMagick as pm
import argparse
import cv2

# Localizando o modulo
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

# Tratando imagem passada como parâmetro
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,	help="path to input image file")
ap.add_argument("-o", "--output", required=True, help="path to output image file")
args = vars(ap.parse_args())
 
# Carregando imagem
img = pm.Image(args["image"])

# Convertendo a imagem para dois canais de cores
img.colorSpace(pm.ColorspaceType.GRAYColorspace)
img.quality(100)
img.sharpen(50, 50)

# Salvando imagem convertida
img.write(args["output"])

# Extraindo o texto da imagem
print( pytesseract.image_to_string(Image.open(args["output"]), lang = 'por')) 