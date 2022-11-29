# Note : environnement virtuel : PCO_env
# --------------------------------------------------------------------------

'''Application de Data Augmentation

Objectif : ouvrir une image, appliquer le modèle entraîné sur l'image,
si : - la labelisation est correcte, sauvegarde les cordonnées dans un fichier txt
     - sinon passe à l'image suivante (sauvegarde l'image dans un autre dossier
                                        afin de la labeliser manuellement)

# Etapes  : 
    # charger le modèle
    # appliquer le modèle sur l'image
    # visualiser le label 
    # récupérer les coordonnées
    # sauvegarder ou passer à l'image suivante '''

# --------------------------------------------------------------------------


# Importations : 
import os
import torch
from PIL import Image 
import PIL 
# git clone Yolov5 puis :
import sys
sys.path.insert(0, './yolov5')


# Chargement du modèle
model = torch.hub.load('ultralytics/yolov5', 'custom', 'model.pt')  # nom du modèle : 'model.pt'


# Chemin des images
chemin = "./test_images/"
# liste contenant les noms de toutes les images du dossier 
dossier_images = os.listdir(chemin) 

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
            file.write(str(liste_coordonnees[x]) + " ")

# Fonction : sauvegarder l'image de base (pour l'entraînement du modèle)
def save_image(nom_image):
    extension = nom_image
    # suppression des extensions dans le nom de l'image
    extensions = ['.PNG', '.png', '.JPG', '.jpg']
    for ext in extensions:
        nom_image = nom_image.replace(ext, "")
    
    # chemin des images sources : variable "chemin"
    # chemin des images de destination
    chemin_destination = "./images_labels/"

    # ouverture de l'image dans le dossier source
    new_image = Image.open(chemin + extension)
    # sauvegarde de l'image dans le dossier de destination
    new_image = new_image.save(chemin_destination + nom_image + ".png")


# Traitement :
for im in dossier_images :
    # on garde le nom de l'image pour la sauvegarde
    nom_image = im
    # Inference
    results = model(chemin + im)
    coordonnees = results.pandas().xyxy[0]

    # Montrer l'image avec le label 
    # results.show()

    # suppression des extensions dans le nom de l'image
    extensions = ['.PNG', '.png', '.JPG', '.jpg']
    for ext in extensions:
        im = im.replace(ext, "")

     # sauvegarder les coordonnées
    save_coordinates(coordonnees, im)

    # sauvegarder l'image (si bien labélisée)
    save_image("1.PNG")

    

    # Sauvegarde de l'image avec le label
    # results.save(save_dir='images_labels', exist_ok = True)




# Inference
#--- results = model(image_name)
# Results
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
# results.xyxy[0]  # im predictions (tensor)
#--- coordonnees = results.pandas().xyxy[0]
# print(coordonnees)
# results.show()






# # appel fonction : sauvegarde des coordonnées dans un fichier txt
# ---save_coordinates(coordonnees, image)



