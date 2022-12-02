# Importations
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import os
import PIL
  
# Création de la fenêtre
root = Tk()
# taille max de la fenêtre
# root.maxsize(600, 400)

# texte
texte = "..............."

# Chemin des images
chemin = "./test_images/"
# liste contenant les noms de toutes les images du dossier 
image_list = os.listdir(chemin) 

# liste pour stocker les images
liste = []


index = 0

def open_image(element):
    my_image = ImageTk.PhotoImage(Image.open(chemin + element).resize((500, 300)))
    liste.append(my_image)
    return my_image 


# création d'un label
my_label = Label(image=open_image(image_list[index]))
my_label.grid(row=0, column=0, columnspan=4)

# espace de texte
text = Label(root, text=texte, font="Helvetica, 20")
text.grid(row=0, column=4, columnspan=1)


# fonction : image suivante
def next(): 
    global my_label
    global button_next
    global button_back
    global index

    if index >= len(image_list) -1 :
        button_next = Button(root, text="suivant >>", state=DISABLED)
    else :
        index += 1

    # Image
    my_label = Label(image = open_image(image_list[index]))

    my_label.grid_forget()
    my_label.grid(row=0, column=0, columnspan=4)
  

    text = Label(root, text=texte, font="Helvetica, 20")
    text.grid(row=0, column=4, columnspan=1)

# image précédente
def back():
    global my_label
    global button_next
    global button_back
    global index
    
    if index == 0 :
        button_back = Button(root, text="<< précédent", state=DISABLED)
    else :
        index -= 1
    
    
    my_label = Label(image = open_image(image_list[index]))
    # button_back = Button(root, text="<< précédent", command=back)

    my_label.grid_forget()
    my_label.grid(row=0, column=0, columnspan=4)
    # button_back.grid(row=1, column=0)

    text = Label(root, text="...", font="Helvetica, 20")
    text.grid(row=0, column=4, columnspan=1)
    
# Fonction : sauvegarder l'image de base (pour l'entraînement du modèle)
def save(chemin_destination="./images_labels/"):
    nom = image_list[index]
    
    # suppression des extensions dans le nom de l'image
    extensions = ['.PNG', '.png', '.JPG', '.jpg']
    for ext in extensions:
        nom_image = image_list[index].replace(ext, "")
     
     # chemin des images de destination
     # chemin_destination = "./images_labels/"

    # ouverture de l'image dans le dossier source
    new_image = Image.open(chemin + nom)
    # sauvegarde de l'image dans le dossier de destination
    new_image = new_image.save(chemin_destination + nom_image + ".png")

    ### Sauvegarder les coordonnées



    # message confirmant la sauvegarde
    text = Label(root, text="Save : Ok", font="Helvetica, 20")
    text.grid(row=0, column=4, columnspan=1)

# déplacer l'image pour la labeliser plus tard
def move(chemin="./im_relabeliser/"):
    save(chemin)

    # message confirmant le déplacement
    text = Label(root, text="Move : Ok", font="Helvetica, 20")
    text.grid(row=0, column=4, columnspan=1)
   

# Bouttons
button_back = Button(root, text="<< précédent", command=back)
button_next = Button(root, text="suivant >>", command=next)
button_exit = Button(root, text="quitter", command=root.destroy)
button_save = Button(root, text="sauvegarder", bg='green', fg='white', command=save) 
button_move = Button(root, text="déplacer", bg='orange', fg='white', command=move) 

# Placement des bouttons
button_back.grid(row=1, column=0)
button_next.grid(row=1, column=4)
button_exit.grid(row=1, column=2)
button_save.grid(row=1, column=3)
button_move.grid(row=1, column=1)


# Lancement de l'application
root.mainloop()