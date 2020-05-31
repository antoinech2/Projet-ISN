############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
#
# Description: Ce fichier contient les données relatives aux ennemis.
# Chaque ennemi est défini ici avec toutes ses caractéristiques.
############################################

enemies = [
{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_1.png",
"image_size" : (20, 20),
"max_health" : (50,0),
"resistance" : (1,0),
"speed" : (0.6,0),
"gain" : (2.5,0),
"life_bar_size" : (17,3)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_3.png",
"image_size" : (25, 25),
"max_health" : (150,15),
"resistance" : (0.9,0.04),
"speed" : (0.65,0.05),
"gain" : (4.5,1),
"life_bar_size" : (19,3)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_4.png",
"image_size" : (30, 30),
"max_health" : (200,25),
"resistance" : (0.85,0.06),
"speed" : (0.7,0.08),
"gain" : (8,2),
"life_bar_size" : (22,3)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_2.png",
"image_size" : (35, 35),
"max_health" : (300,50),
"resistance" : (0.8,0.08),
"speed" : (0.9,0.1),
"gain" : (10,3),
"life_bar_size" : (25,4)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_7.png",
"image_size" : (35, 35),
"max_health" : (200,25),
"resistance" : (0.9,0.02),
"speed" : (1.8,0.2),
"gain" : (15,4),
"life_bar_size" : (25,4)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_9.png",
"image_size" : (32, 32),
"max_health" : (80,20),
"resistance" : (0.95,0.05),
"speed" : (2.7,0.5),
"gain" : (26,5),
"life_bar_size" : (25,4)},

{"name" : "Résistant",
"image_path" : "../res/textures/enemy/virus_5.png",
"image_size" : (45, 45),
"max_health" : (400,75),
"resistance" : (0.75,0.15),
"speed" : (0.55,0.1),
"gain" : (35,15),
"life_bar_size" : (27,5)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_6.png",
"image_size" : (47, 47),
"max_health" : (600,100),
"resistance" : (0.6,0.1),
"speed" : (0.45,0.2),
"gain" : (30,25),
"life_bar_size" : (30,5)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_8.png",
"image_size" : (50, 50),
"max_health" : (150,100),
"resistance" : (0.3,0.03),
"speed" : (0.35,0.07),
"gain" : (100,65),
"life_bar_size" : (33,5)},

{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_10.png",
"image_size" : (55, 55),
"max_health" : (1000,150),
"resistance" : (0.15,0.05),
"speed" : ( 0.2,0.02),
"gain" : (200,20),
"life_bar_size" : (35,7)}
]
