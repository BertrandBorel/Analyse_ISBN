# Programme pour procéder au split_train_val sur un dossier
# Permet de partager les éléments du dossier selon un pourcentage de répartition choisi par l'utilisateur.

# Importations
import os 
import re
import glob
import random
from PIL import Image
from tqdm import tqdm

# chemin des images
chemin_image = "C:/Users/utilisateur/Documents/PCO/Application/New_data/images/"

# chemin des labels
chemin_labels = "C:/Users/utilisateur/Documents/PCO/Application/New_data/labels/"

# Création des listes (images/labels) qui contiennent le nom des fichiers
liste_images = glob.glob(chemin_image + '*.jpg')
images = [os.path.basename(image) for image in liste_images]
labels = [re.sub(r"jpg$", "txt", x.name) for x in os.scandir(chemin_image) if x.name.endswith(".jpg")]

# Dossiers de destination
images_val = "C:/Users/utilisateur/Documents/PCO/Application/New_data/images/val/"
labels_val = "C:/Users/utilisateur/Documents/PCO/Application/New_data/labels/val/"

# Vérifier si les dossiers existent, sinon les créer
if not os.path.exists(images_val):
    os.makedirs(images_val)
if not os.path.exists(labels_val):
    os.makedirs(labels_val)

# Fonction pour obtenir des listes (images/labels) en fonction d'un pourcentage
def split_train_val(liste, pourcentage):
    global val_images_liste, val_labels_liste
    taille = len(liste)
    taille_selection = int(taille * (pourcentage/100))
    val_images_liste = random.sample(list(set(liste)), taille_selection)
    val_labels_liste = [x.replace(".jpg", ".txt") for x in val_images_liste if x.endswith(".jpg")]
    

# fonction pour appliquer le split sur les images
def split_images(liste_images, dossier_source, dossier_destination):
    for nom in tqdm(liste_images) :
        # ouverture de l'image dans le dossier source
        new_image = Image.open(dossier_source + nom)
        # sauvegarde de l'image dans le dossier de destination
        new_image = new_image.save(dossier_destination + nom)
        # suppression de l'image du dossier source une fois sauvegardée dans le dossier de destination
        os.remove(dossier_source + nom)    

# fonction pour appliquer le split sur les labels
def split_labels(liste_labels, dossier_source, dossier_destination):
    for nom in tqdm(liste_labels) :
        ### on déplace simplement le label original dans un autre dossier
        # ...(ce qui supprime le label original)
        os.rename(dossier_source + nom, dossier_destination + nom)


# On procède au split
split_train_val(images, 20)
split_images(val_images_liste, chemin_image, images_val )
split_labels(val_labels_liste, chemin_labels, labels_val)
