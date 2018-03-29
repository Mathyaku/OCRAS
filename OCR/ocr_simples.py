# -*- coding: utf-8 -*-

# Optical Character Recognition (OCR)

# Importando o modulo Pillow para abrir a imagem no script
from PIL import Image 

# Modulo para a utilizacao da tecnologia OCR
import pytesseract 

# Localizando o modulo
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract.exe"

# Extraindo o texto da imagem
print( pytesseract.image_to_string( Image.open('Imagens de Teste/test4.jpg'), lang = 'por' ) ) 