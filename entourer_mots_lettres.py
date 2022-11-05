import cv2
import pytesseract


def detection_caractere(fichier_image) :
    """
    fichier_image : chemin pour accéder au fichier de type image
    affiche à l'écran l'image modifiée dans lequel les caractères sont délimités par un rectangle rouge.
    """
    #lecture d'un fichier
    img = cv2.imread(fichier_image)
    # colorisation
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    """
    extrait le contenu textuel de l'image
    """
    # print(pytesseract.image_to_string(img))
    """
    affiche les coordonnées des contours des lettres
    """
    # print(pytesseract.image_to_boxes(img))
    # hauteur et largeur de l'image
    hImg,wImg,_ =img.shape
    boxes= pytesseract.image_to_boxes(img)
    for b in boxes.splitlines() :
        # transformer le résultat en liste en découpant la chaine avec le séparateur ' '
        b=b.split(' ')
        # texte,x,y,largeur,hauteur
        # print(b)
        # transforme les charctères en entiers
        x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
        cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),1)
        # print(x,y,w,h)
        

    # pour afficher le résultat
    cv2.imshow('Result',img)
    # attendre à oo
    cv2.waitKey(0)

def detection_mot(fichier_image,langue='eng') :
    """
    fichier_image : chemin pour accéder au fichier de type image
    langue : par défaut 'eng' mais on peut mettre 'fra' pour français ou 'rus' pour russe
    affiche à l'écran l'image modifiée dans lequel les mots sont délimités par un rectangle rouge.
    """
    #lecture d'un fichier
    img = cv2.imread(fichier_image)
    # colorisation
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    # hauteur et largeur de l'image
    hImg,wImg,_ =img.shape
    # recherche des mots
    boxes= pytesseract.image_to_data(img,lang=langue)
    for x,b in enumerate(boxes.splitlines()) :
        # x étant l'indice de la ligne
        # l'indice 0 correspond aux entêtes des colonnes
        if x!= 0:
            # transformer le résultat en liste en découpant la chaine avec le séparateur ''
            b=b.split()
            if len(b) == 12 :
            # texte,x,y,largeur,hauteur
                print(b)
            # transforme les charctères en entiers
                x,y,w,h = int(b[6]),int(b[7]),int(b[8]),int(b[9])
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),1)
                cv2.putText(img,b[11],(x,y+25),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            # print(x,y,w,h)
        

    # pour afficher le résultat
    cv2.imshow('Result',img)
    # attendre à oo
    cv2.waitKey(0)
"""
exécution 
"""
if __name__ == '__main__' :

    image_russe='A2_019.jpg'
    image_test='Image_01.jpeg'

    detection_mot(image_russe,langue='rus')