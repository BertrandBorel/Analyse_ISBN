# Interface graphique (Tkinter), pas de classe, version test

'''Objectif : 
    - Rechercher en ligne les infos sur les ISBNS saisis
    - Exporter références dans un csv
    '''

# ------------------------
# Importations
from tkinter import *
import isbnlib
from isbnlib import canonical, meta
import csv
import os.path as path

# ------------------------
# liste de références 
full_references = []

# Création de la fenêtre
fenetre = Tk()

# Personnalisation de la fenêtre
fenetre.title("Application ISBN")
fenetre.geometry("300x300")
fenetre.minsize(1000, 800)
# couleur arrière-plan :
fenetre.config(background='#482b7d')


# ------------------------
# Zone de texte : l'utilisateur doit saisir un ISBN
saisie_ISBN = Entry(fenetre, width=50)
saisie_ISBN.pack()
# ISBN par défaut : pour un exemple
saisie_ISBN.insert(0, "978-1526646651")


# ----------------------------------------------------------------------------------
# LISTE pour sauvegarder les ISBNS saisis
liste_ISBN = []

def ISBN():
    global new_ISBN
    myLabel = Label(fenetre, text="ISBN entré : " + saisie_ISBN.get(), bg="#482b7d", fg="white")
    new_ISBN = saisie_ISBN.get()
    new_ISBN =new_ISBN.replace('-', '')
    # print(new_ISBN)
    # liste_ISBN.append(new_ISBN)
    myLabel.pack()
    research_ISBN(new_ISBN)

myButton = Button(fenetre, text='Recherche', command=ISBN)
myButton.pack()


# ---------------------------------------------------------------------------------- 
# # Création de l'image
# width = 200
# height = 175
# image = PhotoImage(file="image_isbn.PNG").zoom(5).subsample(20)
# canvas = Canvas(fenetre, width=width,height=height, bg='#4065A4')
# canvas.create_image(width/2, height/2, image=image)
# canvas.pack(expand=YES)


# ---------------------------------------------------------------------------------- 
# Rechercher informations avec l'ISBN
def research_ISBN(x):
    global new_ISBN
    global liste_ref
    global full_references 

    liste_ref = []

    try : 

        isbn_research = canonical(x)
        data = isbnlib.meta(isbn_research, service='worldcat')

        print("Résultat : ")
        print("------------------------")

        if len(data["Authors"]) == 1 :
            for x in data["Authors"] :
                liste_ref.append(x)
        else : 
            liste_ref.append(data["Authors"])
            liste_ref.append(data["Title"])
            liste_ref.append(data["Publisher"])
            liste_ref.append(int(data["Year"]))
            liste_ref.append(int(data['ISBN-13']))
            
        full_references.append(liste_ref)
            
    except : 
        erreur_ISBN = Label(fenetre, text="ISBN introuvable ou données incomplètes...", bg="#482b7d", fg="white")
        erreur_ISBN.pack()

    label_reference = Label(fenetre, text=liste_ref, bg="#482b7d", fg="white")

    label_reference.pack()

# ----------------------------------------------------------------------------------
# création d'un csv
def create_csv():
    global nom
    
    nom = nom_csv.get()
    header = ['Auteur(s)', 'Titre', 'Edition', 'Date', 'ISBN']
    with open(nom +'.csv', 'w') as f:
            writer = csv.writer(f)
            # write the header
            writer.writerow(header)
    print("fichier créé avec le nom suivant :", nom)

# ----------------------------------------------------------------------------------
nom_csv = Entry(fenetre, width=50)
nom_csv.pack()
nom_csv.insert(0, "bibliographie")

# ajouter une référence à un csv existant
def ajouter_csv():
    global nom 
    global full_references

    nom = nom_csv.get()

    if path.exists(nom +'.csv'):
        pass
    else:
        create_csv()

    with open(nom +'.csv', 'a', encoding='UTF8') as f:
            for x in (full_references) :
                writer = csv.writer(f)
                writer.writerow(x)

            # message de réussite
            print("Insertion des données réussies.")

    message_ajout = Label(fenetre, text="---------------------------------------------\nInsertion des données réussies.", bg="#482b7d", fg="white")

    message_ajout.pack()

add_button = Button(fenetre, text='Ajouter au fichier csv', command=ajouter_csv)
add_button.pack()


# ----------------------------------------------------------------------------------
# Vider la liste_ref
def clean_liste_ref():
    global liste_ref
    liste_ref = []

    message_clean = Label(fenetre, text="---------------------------------------------\n Liste nettoyée !", bg="#482b7d", fg="white")

    message_clean.pack()

add_button = Button(fenetre, text='Réinitialiser ma liste', command=clean_liste_ref)
add_button.pack()


fenetre.mainloop()