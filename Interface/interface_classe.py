# Interface avec Tkinter et une classe

# Objectif : Interroger BDD pour obtenir un résultat

# importation
import tkinter as tk
import mysql.connector as msql
from mysql.connector import Error

# Classe principale
class Application(tk.Tk):
    

    def __init__(self):
        tk.Tk.__init__(self)
        self.interface()


    def interface(self):
        global saisie_ISBN
        global liste_ref

        self.label = tk.Label(self, text="Entrez l'ISBN d'un ouvrage :", bg="#482b7d", fg="white")
        saisie_ISBN = tk.Entry(self, width=50)
        self.label.pack()
        saisie_ISBN.pack()
        self.myButton = tk.Button(self, text='Recherche', command=self.ISBN)
        self.myButton.pack()
        self.bouton = tk.Button(self, text="Quitter", command=self.quit)
        self.bouton.pack()
        liste_ref = []


    def ISBN(self):
        global new_ISBN

        self.myLabel = tk.Label(self, text="ISBN entré : " + saisie_ISBN.get(), bg="#482b7d", fg="white")
        new_ISBN = saisie_ISBN.get()
        new_ISBN = new_ISBN.replace('-', '')
        self.myLabel.pack()
        self.requete(new_ISBN)

# ---------------------------------------------------------------
# Méthodes pour bdd :

    def connexion(self):
        global conn
        try:
            conn = msql.connect(host='host', user='user', port='port', password='password', database='database')
            if conn.is_connected():
                print("Connexion réussie !")
            # cursor = conn.cursor()
        except Error as e:
            error_label = tk.Label(self, text="Erreur : impossible de se connecter à la bdd...", bg="white", fg="red")
            error_label.pack()

    def deconnexion(self):
        global conn
        conn.close()
        print("Déconnexion réussie.")
        
    
    def requete(self, isbn):
        global conn
        global liste_ref
        global new_ISBN
        
        self.connexion()

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


        self.deconnexion() 

        label_reference = tk.Label(self, text=ref, bg="#482b7d", fg="white")

        label_reference.pack()




if __name__ == "__main__":
    app = Application()
    app.title("Application ISBN")
    app.minsize(1000, 800)
    app.config(background='#482b7d')
    app.mainloop()