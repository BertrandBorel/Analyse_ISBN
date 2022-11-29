# Traitement pour une seule image :

# Importations : 
import torch
# git clone Yolov5 puis :
import sys
sys.path.insert(0, './yolov5')


# Chargement du modèle
# model = torch.load('model.pt')
model = torch.hub.load('ultralytics/yolov5', 'custom', 'model.pt')  # nom du modèle : 'model.pt'


# Pour une image : 
image = "6" # nom de l'image (plus facile pour sauvegarder les labels)
# extension de l'image
extension = ".png"
# nom complet de l'image
image_name = image + extension # for image in dossier_images : 


# Inference
results = model(image_name)
# Results : 
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
# results.xyxy[0]  # im predictions (tensor)
coordonnees = results.pandas().xyxy[0]
# results.show()


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

# # appel fonction : sauvegarde des coordonnées dans un fichier txt
save_coordinates(coordonnees, image)
