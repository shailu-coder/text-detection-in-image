# Download and install google tesseract OCR
# by this link https://github.com/UB-Mannheim/tesseract/wiki
# For any kind of help contact www.instagram.com/python_coderz_
import pytesseract as tess
# tess.pytesseract.tesseract_cmd = r'C:\Users\sk\AppData\Local\Tesseract-OCR\tesseract.exe' #put here full path with exe from your system
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #put here full path with exe
from tkinter import *
from tkinter import filedialog as fd
import os
from PIL import Image
import random
import pyperclip
import pyautogui
try:
    img=Image.open('11.jpg')
    x= tess.image_to_string(img)
    print(x)
    pyperclip.copy(x)#after gettubg text it will be copied in your system clipboard
except Exception as e:
    print(e)
