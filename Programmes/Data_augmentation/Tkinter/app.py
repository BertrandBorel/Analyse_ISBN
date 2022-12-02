# gallerie d'images avec Tkinter

# Importations
from tkinter import *
from PIL import ImageTk, Image
import os

# Création de la fenêtre
root = Tk()
root.title('Data Augmentation')
# icône : root.iconbitmap("chemin de l'icône")


# liste d'images à afficher :
# Chemin des images
chemin = "./test_images/"
# liste contenant les noms de toutes les images du dossier 
image_list = os.listdir(chemin) 
longueur_liste = len(image_list)
print(longueur_liste)

# index des images (+/-)
index = 0


# image
# my_img = ImageTk.PhotoImage(Image.open("chemin"))
my_img = Image.open(chemin + image_list[index])
resize_image = my_img.resize((500, 200))
img = ImageTk.PhotoImage(resize_image) 


# création d'un label
my_label = Label(image=img)
my_label.grid(row=0, column=0, columnspan=4)


# Fonctions

def next(): #image_number
    global my_label
    global button_next
    global button_back
    global index

    if index == longueur_liste -1 :
        button_next = Button(root, text="suivant >>", state=DISABLED)
    else :
        index += 1


    # new_img = Image.open(chemin + image_list[index])
    # resize_image = new_img.resize((500, 200))
    # test = ImageTk.PhotoImage(resize_image) 
    
    my_label.grid_forget()
    my_label = Label(image = chemin + image_list[index])
    button_back = Button(root, text="<< précédent", command=back)
    button_next = Button(root, text="suivant >>", command=next)

    my_label.grid(row=0, column=0, columnspan=4)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=4)

def back():
    global my_label
    global button_next
    global button_back
    global index
    
    if index == 0 :
        button_back = Button(root, text="<< précédent", state=DISABLED)
    else :
        index -= 1


    # new_img = Image.open()
    # resize_image = new_img.resize((500, 200))
    # test = ImageTk.PhotoImage(resize_image) 
    
    my_label.grid_forget()
    my_label = Label(image = chemin + image_list[index])
    button_back = Button(root, text="<< précédent", command=back)
    button_next = Button(root, text="suivant >>", command=next)

    
    my_label.grid(row=0, column=0, columnspan=4)
    button_back.grid(row=1, column=0)
    button_exit.grid(row=1, column=4)


    
def save():
    pass

def move():
    pass



# Bouttons
button_back = Button(root, text="<< précédent", command=back)
button_next = Button(root, text="suivant >>", command=next)
button_exit = Button(root, text="quitter", command=root.destroy)
button_save = Button(root, text="sauvegarder", command=save()) 
button_move = Button(root, text="déplacer", command=move()) 

# Placement des bouttons
button_back.grid(row=1, column=0)
button_next.grid(row=1, column=4)
button_exit.grid(row=1, column=2)
button_save.grid(row=1, column=3)
button_move.grid(row=1, column=1)


# lancement de l'application
root.mainloop()