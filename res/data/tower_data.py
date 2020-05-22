
#SYNTAXE:
#["NOM", "IMAGE PATH", (WIDTH, HEIGHT), (MAX_HEALTH, MAX_HEALTH_RANDOM_RANGE), (RESISTANCE, RESISTANCE_RANDOM_RANGE),
#(SPEED, SPEED_RANDOM_RANGE), (GAIN, GAIN_RANDOM_RANGE), (LIFE_BAR_WIDTH, LIFE_BAR_HEIGHT)]
#enemies = [\
#["Basique", "../res/textures/enemy/virus_rouge.png", (40, 40), (100,0), (100,0), (1,0), (2,0), (25,4)]\
#]

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
"life_bar_range" : 30
}]
