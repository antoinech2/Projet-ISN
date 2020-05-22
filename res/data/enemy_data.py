
#SYNTAXE:
#["NOM", "IMAGE PATH", (WIDTH, HEIGHT), (MAX_HEALTH, MAX_HEALTH_RANDOM_RANGE), (RESISTANCE, RESISTANCE_RANDOM_RANGE),
#(SPEED, SPEED_RANDOM_RANGE), (GAIN, GAIN_RANDOM_RANGE), (LIFE_BAR_WIDTH, LIFE_BAR_HEIGHT)]
#enemies = [\
#["Basique", "../res/textures/enemy/virus_rouge.png", (40, 40), (100,0), (100,0), (1,0), (2,0), (25,4)]\
#]

enemies = [
{"name" : "Basique",
"image_path" : "../res/textures/enemy/virus_rouge.png",
"image_size" : (40, 40),
"max_health" : (100,0),
"resistance" : (1,0),
"speed" : (1,0),
"gain" : (2,0),
"life_bar_size" : (25,4)
}]
