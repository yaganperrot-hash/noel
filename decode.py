from stegano import lsb

# Nom du fichier contenant le message caché
fichier_a_decoder = "sapinmodif.png"

# Utilisation de la fonction de révélation
url_revelee = lsb.reveal(fichier_a_decoder)

# Affichage de l'URL
print("--- Résultat du Décodage ---")
print(url_revelee)