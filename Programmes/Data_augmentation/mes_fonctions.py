'''
Fichier stockant les différentes fonctions pour le bon fonctionnement du script 'app.py
-------------------------------------------------------------------------------------------
'''
from PIL import Image 

'''Fonction à retravailler, code plus efficace'''
# fonction pour convertir le label en format Yolov5
def convertir_nombre(nombre):
    
    # on récupère les nombres entiers
    arrondi = round(nombre)
    # conversion en str
    conversion = str(arrondi)
    
    # en fonction de la longueur on applique les changements
    if len(conversion) == 1 :
        conversion = 10
    elif len(conversion) == 2 :
        conversion = 100
    elif len(conversion) == 3 :
        conversion = 1000 
    elif len(conversion) == 4 :
        conversion = 10000
    elif len(conversion) == 5 :
        conversion = 100000
    else :
        print("Erreur. Nombre trop grand.") 
              
    return nombre / conversion



# Fonction : sauvegarde les coordonnées dans un fichier texte :
def save_coordinates(new_coordinates, image_name):
    # On récupère les coordonnées dans une liste
    liste_coordonnees = [x for x in new_coordinates.iloc[0]]
    # sauvegarder les nouvelles coordonnées dans un fichier txt
    with open("labels/" + image_name + ".txt", 'w') as file :
        # insertion de la classe
        file.write("0 ")
        # insertion des coordonnées
        for x in range(4) : 
            # conversion du nombre  (type : 456,123 en 0,456123)
            nombre = convertir_nombre(liste_coordonnees[x])
            file.write(str(nombre) + " ")


