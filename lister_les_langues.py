from PIL import Image
import pytesseract
import numpy as np
"""
lister les langues reconnues
"""
lang=pytesseract.get_languages()

print(lang)