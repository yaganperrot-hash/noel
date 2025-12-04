from stegano import lsb

# Paramètres
url_a_cacher = "https://imgur.com/a/ob7i4Iz"
image_source = "sapinmodified.png"
image_sortie = "sapinmodif.png"

try:
    # Action de cacher
    image_secret = lsb.hide(image_source, url_a_cacher)
    
    # Sauvegarde
    image_secret.save(image_sortie)
    print(f"L'URL a été cachée avec succès dans {image_sortie}")

except FileNotFoundError:
    print(f"Erreur : L'image source '{image_source}' est introuvable.")