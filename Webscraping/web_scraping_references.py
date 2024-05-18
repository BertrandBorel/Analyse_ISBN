import csv
import requests
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm_notebook



# def creation_csv(nom): # il suffit d'indiquer le nom du csv (sans l'extension)
#     with open(nom +'.csv', 'w') as f:
#             writer = csv.writer(f)
#             # write the header
#             writer.writerow(header)
#     print("fichier créé avec le nom suivant :", nom)


def creation_csv(nom):
    '''Création d'un nouveau fichier CSV avec un en-tête spécifique.
    
    Le paramètre 'nom' permet de choisir le nom du fichier (sans l'extension .csv).
    Il n'y a pas de nom par défaut afin de ne pas écraser un fichier précédemment créé par erreur.
    
    Args:
        nom (str): Le nom du fichier CSV à créer (sans l'extension .csv).
    '''
    header = ['Auteur(s)', 'Titre', 'Edition', 'Date', 'ISBN']
    
    try:
        with open(nom + '.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
        print("Fichier créé avec le nom suivant :", nom + '.csv')
    except Exception as e:
        print(f"Une erreur est survenue lors de la création du fichier : {e}")



    
    
    

  
def web_scraping(nb_livres=5000, nombre=185000, nom_csv = 'ajout_fonction', site = 'https://www.leslibraires.fr/livre/'):
    '''Fonction permettant d'interroger la page d'un livre et d'en récupérer les informations. 
Si les informations ne sont pas trouvées sur la page, on passe alors à un autre livre.
Fonctionne par incrémentation de chaque page web.
Les paramètres sont :
  - le nombre de livres récupérés à chaque passage (par défaut : 5000, plus d'une heure de traitement)
  - le nombre de la page à laquelle le web scraping commence (il faut l'augmenter par défaut de 5000 à chaque passage)
  - le nom du csv où seront stockées les données
  - le site web (par défaut les libraires.fr)'''
    liste_totale = []
    
    for livre in tqdm_notebook(range(nb_livres)) : 
        erreur = 0
        
        try : 
            url = site + str(nombre)
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')

            liste = []

            # auteur 
            auteur = soup.find("h2")
            auteur = auteur.text.strip('\n')
            liste.append(auteur)

            # titre
            titre = soup.find("h1")
            titre = titre.text.strip('\n')
            liste.append(titre)

            # edition
            edition = soup.find("h3")
            edition = edition.text.strip('\n')
            liste.append(edition)

            # date
            date = soup.findAll("dd")
            # on récupère la date dans une variable temporaire
            var_temp = date[5].text
            # on split la date et on ne récupère que l'année
            split = var_temp.split("/")
            date = split[-1]
            # # on ajoute la date (format : int) à la liste
            # liste.append(int(date))
            liste.append(date)

            # ISBN
            # Récupérer l'isbn
            info = soup.findAll("dd")
            # on récupère l'isbn dans une variable temporaire
            isbn = info[2].text
            liste.append(isbn)

            liste_totale.append(liste)

            nombre += 1

        except :

            nombre += 1
            erreur += 1


    print("Nb d'erreurs :", erreur)

    # insérer les informations pour chaque livre (à partir de la liste totale)
    with open(nom_csv+'.csv', 'a', encoding='UTF8') as f:
            for x in tqdm_notebook(liste_totale) :
                writer = csv.writer(f)
                writer.writerow(x)

            # message de réussite
            print("Insertion des données réussies.")
    
    
    
