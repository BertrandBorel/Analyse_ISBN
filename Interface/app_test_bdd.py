# Interface graphique (Tkinter), sans classe

'''Objectifs :
    - Interroger notre base de données
    - Inscrire les résultats dans un csv'''

#--------------------
# Importations
from tkinter import *
import csv
import os.path as path
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

#--------------------
liste_ref = []

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

# Zone de texte : l'utilisateur doit saisir un ISBN
saisie_ISBN = Entry(fenetre, width=50)
saisie_ISBN.pack()
# ISBN par défaut : pour un exemple
saisie_ISBN.insert(0, "9782130466260")


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
    requete(new_ISBN)

myButton = Button(fenetre, text='Recherche', command=ISBN)
myButton.pack()


# # Rechercher informations avec l'ISBN
# def research_ISBN_database(x):
#     global new_ISBN
#     global liste_ref
#     requete(new_ISBN)
#     print("ok")

    # label_reference = Label(fenetre, text=ref_bdd, bg="#482b7d", fg="white")

    # label_reference.pack()


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


# ---------------------------------------------------------------
# Fonctions pour bdd :

def connexion():
    global conn
    try:
        conn = msql.connect(host='host', user='user', port='port', password='password', database='database')
        if conn.is_connected():
            print("Connexion réussie !")
        # cursor = conn.cursor()
    except Error as e:
        error_label = Label(fenetre, text="Erreur : impossible de se connecter à la bdd...", bg="white", fg="red")
        error_label.pack()

def deconnexion():
    global conn
    conn.close()
    print("Déconnexion réussie.")
    
def requete(isbn):
    global conn
    global liste_ref
    # global new_ISBN
    
    connexion()


    try:
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM ref WHERE ISBN = %s """, (isbn, )) 
        rows = cursor.fetchall() 
        for row in rows: 
            ref = '{1}, {2}, {3}, {4}, {0}'.format(row[0], row[1], row[2], row[3], row[4])
            print(ref)
            liste_ref.append(ref)
    except Error as e:
        print("Erreur : impossible d'afficher un résultat.", e) 


    deconnexion() 

    label_reference = Label(fenetre, text=ref, bg="#482b7d", fg="white")

    label_reference.pack()

   # return liste_ref


# ------------------
# Test :

fenetre.mainloop()