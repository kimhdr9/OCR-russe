from PIL import Image
import pytesseract
import numpy as np
from googletrans import Translator
import sys

"""
l'image est bruitée
"""
# filename = 'Image_02.png'
try :
    filename=sys.argv[1]
    img1 = np.array(Image.open(filename))
    text = pytesseract.image_to_string(img1,lang='rus')


    # affiche le contenu du texte 
    print(text)
except OSError as e :
    print(f'le script a besoin du nom du fichier image code :{e}')
"""
mettre la valeur à True pour obtenir une traduction
"""
avec_traduction=False
if avec_traduction :
    traduction = Translator()

    out = traduction.translate(text,dest="en")

    # traduit le texte en anglais.
    print(out.text)