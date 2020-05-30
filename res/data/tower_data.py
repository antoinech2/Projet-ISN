############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
#
# Description: Ce fichier contient les données relatives aux tours.
# Chaque tour est définie ici avec toutes ses caractéristiques.
############################################

towers = [
{"name" : "Basique",
"image_path" : "../res/textures/tower/tower_1.png",
"image_size" : (40, 40),
"range" : 2,
"attack_damage" : (20,3),
"attack_cooldown" : (1,0.2),
"attack_enemies" : (1,0),
"shoot_max" : 100,
"shoot_reduction": (1,0),
"cost" : 15,
"life_bar_range" : 22,
"projectile_speed" : (2.5,0.5)}
]
