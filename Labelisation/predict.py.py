# Prédictions sur une seule image

# Prédiction sur de nouvelles images

# problème de labels : convertir les labels au même format
# ouvrir un dossier = récupérer nom dans une liste

# importations
import torch
import math
from tqdm import tqdm
import os 
import glob 
import numpy as np
from PIL import Image, ImageDraw
import cv2

# Chargement du modèle
# model = torch.hub.load('ultralytics/yolov5', 'custom', 'C:/Users/utilisateur/Downloads/75b_60e/best.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', 'C:/Users/utilisateur/Desktop/data_test/best.pt')

# chemin des images
chemin_image = "C:/Users/utilisateur/Documents/PCO/Application/Re_labeliser/"




liste_images = glob.glob(chemin_image + '*.jpg')
images = [os.path.basename(image) for image in liste_images]



# dossier pour sauvegarder les nouveaux labels
labels_dir = "C:/Users/utilisateur/Documents/PCO/Application/Predictions/labels_pred/"
# labels_dir = "C:/Users/utilisateur/Documents/PCO/Application/new_labels/labels/"

# chemin des images
images_dir = "C:/Users/utilisateur/Documents/PCO/Application/Predictions/images_pred/"
# images_dir = "C:/Users/utilisateur/Documents/PCO/Application/new_labels/images/"





# faire une prédiction sur chaque image
for image in tqdm(images, dynamic_ncols=True) :
    # Charger l'image
    img = Image.open(chemin_image + image)
    # Récupérer la hauteur et la largeur de l'image
    width, height = img.size
    
    results = model(chemin_image + image)
    coordonnees = results.pandas().xyxy[0].iloc[:, :4]

    liste = []

    for row in coordonnees.itertuples():
        x1 = row[1]
        y1 = row[2]
        x2 = row[3]
        y2 = row[4]

        X = round((x1 + x2) / 2 / width, 6)
        Y = round((y1 + y2) / 2 / height, 6)
        W = round((x2 - x1) / width, 6)
        H = round((y2 - y1) / height, 6)
        
        liste.append([0, X, Y, W, H])

        # Code à tester ! 
        # results = model(chemin_image + image)
        # coordonnees = results.pandas().xyxy[0].iloc[:, :4]

        # X = np.round((coordonnees.iloc[:, [0, 2]].mean(axis=1)) / width, 6)
        # Y = np.round((coordonnees.iloc[:, [1, 3]].mean(axis=1)) / height, 6)
        # W = np.round((coordonnees.iloc[:, 2] - coordonnees.iloc[:, 0]) / width, 6)
        # H = np.round((coordonnees.iloc[:, 3] - coordonnees.iloc[:, 1]) / height, 6)

        # liste = np.concatenate((np.zeros((len(X), 1)), np.column_stack((X, Y, W, H))), axis=1).tolist()



    # sauvegarde l'image dans un fichier
    results.save(save_dir=images_dir, exist_ok=True, labels=False)
    # Masque les labels lors de la prédiction

        
    # Sauvegarder les coordonnées dans un fichier texte
    with open(labels_dir + image.replace("jpg", "txt"), 'w') as f:
        # ajouter un 0 au début de chaque ligne
        liste = [ligne for ligne in liste]
        f.writelines(" ".join(str(x) for x in ligne) + "\n" for ligne in liste)



