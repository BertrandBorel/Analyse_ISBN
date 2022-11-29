# Sauvegarder une image



from PIL import Image 
import PIL 

def save_image(nom_image):
    extension = nom_image
    # suppression des extensions dans le nom de l'image
    extensions = ['.PNG', '.png', '.JPG', '.jpg']
    for ext in extensions:
        nom_image = nom_image.replace(ext, "")
    
    # chemin des images sources :
    chemin_source = "./test_images/"
    # chemin des images de destination
    chemin_destination = "./images_labels/"

    # ouverture de l'image dans le dossier source
    new_image = Image.open(chemin_source + extension)
    # sauvegarde de l'image dans le dossier de destination
    new_image = new_image.save(chemin_destination + nom_image + ".png")




save_image("1.PNG")