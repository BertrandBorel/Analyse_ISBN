'''MAJ de l'application de labelisation

- prédictions obtenues avec yolo
- décider si :
        - save : save image_true  (+ delete image_pred) AND save label
        - move : save image_true (+ delete image_pred) AND delete label
        - delete : delete image_pred AND delete label'''


# Importations
import tkinter as tk
from PIL import Image, ImageTk
import os


  
# Création de la fenêtre
root = tk.Tk()
# taille max de la fenêtre
# root.maxsize(600, 400)

# chemin général
chemin_general = "C:/Users/utilisateur/Documents/PCO/Application/"

# Chemin des images
chemin = chemin_general + "Predictions/images_pred/"
# liste contenant les noms de toutes les images du dossier 
image_list = os.listdir(chemin) 

# liste pour stocker les images
liste = []



index = 0

def open_image(element):
    my_image = ImageTk.PhotoImage(Image.open(chemin + element).resize((500, 300)))
    liste.append(my_image)
    return my_image 


# création d'un label = afficher l'image
my_label = tk.Label(image=open_image(image_list[index]))
my_label.grid(row=0, column=0, columnspan=4)



# fonction : image suivante
def next(): 
    global my_label, button_next, button_back, index

    if index >= len(image_list) -1 :
        button_next = tk.Button(root, text="suivant >>", state=tk.DISABLED)
    else :
        index += 1

    # Image
    my_label = tk.Label(image = open_image(image_list[index]))
    my_label.grid_forget()
    my_label.grid(row=0, column=0, columnspan=4)
  

# image précédente
def back():
    global my_label, button_next, button_back, index
    
    if index == 0 :
        button_back = tk.Button(root, text="<< précédent", state=tk.DISABLED)
    else :
        index -= 1
    
    my_label = tk.Label(image = open_image(image_list[index]))


    my_label.grid_forget()
    my_label.grid(row=0, column=0, columnspan=4)


    text = tk.Label(root, text="", font="Helvetica, 20")
    text.grid(row=0, column=4, columnspan=1)
    
# Fonction : sauvegarder l'image de base (pour l'entraînement du modèle)
def save(chemin_destination=chemin_general+"New_data/images/", chemin_labels=chemin_general+"New_data/labels/"):
    nom = image_list[index]

    # # suppression des extensions dans le nom de l'image
    # extensions = ['.PNG', '.png', '.JPG', '.jpg']
    # for ext in extensions:
    nom_image = image_list[index].replace(".jpg", "")

    # ouverture de l'image dans le dossier source
    new_image = Image.open(chemin_general+"Images_true/" + nom)
    # sauvegarde de l'image dans le dossier de destination
    new_image = new_image.save(chemin_destination + nom_image + ".jpg")

    # suppression de l'image_pred une fois sauvegardée 
    os.remove(chemin + nom)
    # suppression de l'image_true une fois sauvegardée 
    os.remove(chemin_general+"Images_true/" + nom)


    ### Sauvegarder les coordonnées = on déplace simplement le label original dans 
    # ... un autre dossier (ce qui supprime le label original)
    new_name = nom.replace(".jpg", ".txt")
    os.rename(chemin_general+"Predictions/labels_pred/" + new_name, chemin_labels + new_name)

    # # mettre à jour la liste d'images = éviter des erreurs pour back/next image
    # image_list = os.listdir(chemin) 

    # passer à l'image suivante
    next()

# déplacer l'image pour la labeliser plus tard
def move(chemin=chemin_general+"Re_labeliser/"):
    nom = image_list[index]
    nom_image = image_list[index].replace(".jpg", "")
    new_image = Image.open(chemin_general+"Images_true/" + nom)
    # sauvegarde de l'image dans le dossier de destination
    new_image = new_image.save(chemin + nom_image + ".jpg")

    # Suppression des images
    os.remove(chemin_general+"Images_true/" + nom)
    os.remove(chemin_general+"Predictions/images_pred/" + nom)

    # Suppression du label
    new_name = nom.replace(".jpg", ".txt")
    os.remove(chemin_general+"Predictions/labels_pred/" + new_name)
    # image suivante
    next()



# supprimer l'image
def delete():
    nom = image_list[index]
    # Suppression des images
    os.remove(chemin_general+"Images_true/" + nom)
    os.remove(chemin_general+"Predictions/images_pred/" + nom)
    # Suppression du label
    new_name = nom.replace(".jpg", ".txt")
    os.remove(chemin_general+"Predictions/labels_pred/" + new_name)
    # image suivante
    next()

   

# Bouttons
button_back = tk.Button(root, text="<<", command=back)
button_next = tk.Button(root, text=">>", command=next)
button_exit = tk.Button(root, text="delete", bg='red', fg='white', command=delete)
button_save = tk.Button(root, text="save", bg='green', fg='white', command=save) 
button_move = tk.Button(root, text="move", bg='orange', fg='white', command=move) 

# Placement des bouttons
button_back.grid(row=1, column=0)
button_next.grid(row=1, column=4)
button_exit.grid(row=1, column=2)
button_save.grid(row=1, column=3)
button_move.grid(row=1, column=1)


# Lancement de l'application
root.mainloop()

