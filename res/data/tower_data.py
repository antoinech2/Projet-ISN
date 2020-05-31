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
"image_size" : (35, 35),
"range" : 1.75,
"attack_damage" : (20,3),
"attack_cooldown" : (1,0.2),
"attack_enemies" : (1,0),
"shoot_max" : 100,
"shoot_reduction": (1,0),
"cost" : 30,
"life_bar_range" : 19,
"projectile_speed" : (2.5,0.5)},

{"name" : "Grande portée",
"image_path" : "../res/textures/tower/tower_3.png",
"image_size" : (55, 55),
"range" : 6,
"attack_damage" : (10,5),
"attack_cooldown" : (1.3,0.3),
"attack_enemies" : (2,0),
"shoot_max" : 150,
"shoot_reduction": (1,0),
"cost" : 60,
"life_bar_range" : 29,
"projectile_speed" : (3,0.5)},

{"name" : "Améliorée",
"image_path" : "../res/textures/tower/tower_2.png",
"image_size" : (40, 40),
"range" : 2.5,
"attack_damage" : (26,4),
"attack_cooldown" : (0.8,0.15),
"attack_enemies" : (2,1),
"shoot_max" : 300,
"shoot_reduction": (1,0.5),
"cost" : 95,
"life_bar_range" : 22,
"projectile_speed" : (2.5,0.5)},

{"name" : "Immortel",
"image_path" : "../res/textures/tower/tower_4.png",
"image_size" : (37, 37),
"range" : 2,
"attack_damage" : (22,3),
"attack_cooldown" : (1.3,0.2),
"attack_enemies" : (1,0),
"shoot_max" : 1500,
"shoot_reduction": (1,0),
"cost" : 110,
"life_bar_range" : 20,
"projectile_speed" : (3,0.5)},

{"name" : "Tir multiple",
"image_path" : "../res/textures/tower/tower_8.png",
"image_size" : (50, 50),
"range" : 1.5,
"attack_damage" : (17,5),
"attack_cooldown" : (1.5,0.3),
"attack_enemies" : (6,3),
"shoot_max" : 300,
"shoot_reduction": (6,2),
"cost" : 150,
"life_bar_range" : 27,
"projectile_speed" : (4,0.5)},

{"name" : "Aléatoire",
"image_path" : "../res/textures/tower/tower_6.png",
"image_size" : (30, 30),
"range" : 2.25,
"attack_damage" : (20,20),
"attack_cooldown" : (1.5,1.5),
"attack_enemies" : (2,2),
"shoot_max" : 1000,
"shoot_reduction": (10,10),
"cost" : 175,
"life_bar_range" : 17,
"projectile_speed" : (2.5,1.5)},

{"name" : "Gros dégats",
"image_path" : "../res/textures/tower/tower_5.png",
"image_size" : (55, 55),
"range" : 1.5,
"attack_damage" : (70,15),
"attack_cooldown" : (2,0.5),
"attack_enemies" : (2,1),
"shoot_max" : 250,
"shoot_reduction": (1,0.75),
"cost" : 250,
"life_bar_range" : 29,
"projectile_speed" : (1.5,0.5)},

{"name" : "Mitraillette à distance",
"image_path" : "../res/textures/tower/tower_10.png",
"image_size" : (80, 80),
"range" : 7,
"attack_damage" : (3.5,0.5),
"attack_cooldown" : (0.2,0.07),
"attack_enemies" : (1,0),
"shoot_max" : 1500,
"shoot_reduction": (1,0.15),
"cost" : 300,
"life_bar_range" : 42,
"projectile_speed" : (3,2.5)},

{"name" : "Sniper",
"image_path" : "../res/textures/tower/tower_9.png",
"image_size" : (85, 85),
"range" : 6.5,
"attack_damage" : (300,50),
"attack_cooldown" : (5,2),
"attack_enemies" : (1,0),
"shoot_max" : 250,
"shoot_reduction": (2,1),
"cost" : 350,
"life_bar_range" : 44,
"projectile_speed" : (1,0.5)},

{"name" : "Proximité",
"image_path" : "../res/textures/tower/tower_11.png",
"image_size" : (20, 20),
"range" : 1,
"attack_damage" : (50,15),
"attack_cooldown" : (2,0.5),
"attack_enemies" : (1,1),
"shoot_max" : 100,
"shoot_reduction": (1,0.7),
"cost" : 450,
"life_bar_range" : 12,
"projectile_speed" : (1,0.2)},

{"name" : "Mitraillette courte portée",
"image_path" : "../res/textures/tower/tower_12.png",
"image_size" : (35, 35),
"range" : 1.25,
"attack_damage" : (4,1),
"attack_cooldown" : (0.05,0.015),
"attack_enemies" : (1,0),
"shoot_max" : 2500,
"shoot_reduction": (1,0.3),
"cost" : 500,
"life_bar_range" : 19,
"projectile_speed" : (4,2.5)},

{"name" : "Ultime",
"image_path" : "../res/textures/tower/tower_7.png",
"image_size" : (64, 64),
"range" : 3,
"attack_damage" : (45,10),
"attack_cooldown" : (0.8,0.2),
"attack_enemies" : (3,1),
"shoot_max" : 5000,
"shoot_reduction": (5,2.5),
"cost" : 1000,
"life_bar_range" : 34,
"projectile_speed" : (4,0.5)},
]
