############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.1
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.2
#
# Script de génération aléatoire du chemin
#
# Description: Algorithme de création aléatoire du chemin
# Ce script génère un grand nombre de chemin aléatoires
# jusqu'à ce qu'il soit suffisamment long pour être choisi.
############################################

############################################
# Importation des modules
import random
############################################

############################################
# Définition des constantes
force_space_between_path = True
path_coords = []
min_path_length = 30

#Constantes de direction:
DIR_NORTH = 1
DIR_SOUTH = 2
DIR_EAST = 3
DIR_WEST = 4
############################################

############################################
# Définition des fonctions locales:

def CalculateNewStartPosition(map_size):
	"Fonction de calcul du point de départ du chemin sur un bord de la carte"
	if random.randint(0,1) == 1:       		#X=1 ou X=taille
		if random.randint(0,1) == 1:		#X=1
			x_start = 1
			direction_start = DIR_SOUTH
		else:
			x_start = map_size[0]			#X=taille
			direction_start = DIR_NORTH
		y_start = random.randint(2,map_size[1]-1)
	else:									#Y=1 ou Y=taille
		if random.randint(0,1) == 1:
			y_start = 1						#Y=1
			direction_start = DIR_EAST
		else:
			y_start = map_size[1]			#Y=taille
			direction_start = DIR_WEST
		x_start = random.randint(2,map_size[0]-1)

	start_coords = (x_start,y_start)
	return start_coords, direction_start

#number_calculation = 0

def CalculateNewPath(map_size):
	"Fonction de calcul aléatoire d'un chemin qui correspond aux critères donnés."
	global path_coords
	while len(path_coords) < min_path_length:
		#if number_calculation%10000 == 0:
		#	print("Tentatives:",number_calculation)
		#number_calculation += 1

		# Initialisation de la génération d'un chemin
		start_coords, direction_start = CalculateNewStartPosition(map_size)
		path_coords = []
		map = []
		for loop in range (map_size[0]+2):
			map.append([0]*(map_size[1]+2))

		path_coords.append(start_coords)
		map[start_coords[0]][start_coords[1]] = 1
		number_voisins = 2
		stop_generation = False
		direction = direction_start

		while stop_generation == False:
			number_change_direction = 0
			while not ((number_voisins < 2) and (map[current_case[0]][current_case[1]] == 0)):
				current_case = list(path_coords[-1])
				if direction == DIR_NORTH:
					#Direction: Nord
					current_case[0] -= 1
				elif direction == DIR_SOUTH:
					#Direction: Sud
					current_case[0] += 1
				elif direction == DIR_EAST:
					#Direction: Est
					current_case[1] += 1
				elif direction == DIR_WEST:
					#Direction: Ouest
					current_case[1] -= 1

				number_voisins = 0
				if force_space_between_path:
					if map[current_case[0]+1][current_case[1]]:
						number_voisins +=1
					if map[current_case[0]-1][current_case[1]]:
						number_voisins +=1
					if map[current_case[0]][current_case[1]+1]:
						number_voisins +=1
					if map[current_case[0]][current_case[1]-1]:
						number_voisins +=1

				if number_change_direction == 4:
					path_coords = []
					stop_generation = True
					break
				else:
					number_change_direction += 1
					if direction == 4:
						direction = 1
					else:
						direction += 1
				direction = random.randint(1,4)
			if (current_case[0] == 1) or (current_case[0] == map_size[0]) or (current_case[1] == 1) or (current_case[1] == map_size[1]):
				stop_generation = True

			path_coords.append((current_case[0],current_case[1]))
			map[current_case[0]][current_case[1]] = 1
	return path_coords

# print(path_coords)
#
# for row in range (1,map_size[0]+1):
# 	for column in range (1,map_size[1]+1):
# 		if path_coords[0] == (column,row):
# 			print("D", end="")
# 		elif path_coords[-1] == (column,row):
# 			print("A", end="")
# 		elif (column,row) in path_coords:
# 			print("°", end="")
# 		else:
# 			print(".", end="")
# 	print("")
#
# for row in range (map_size[0]+2):
# 	for column in range (map_size[1]+2):
# 		print(map[column][row], end="")
# 	print("")
#
# print("Génération terminée en",number_calculation,"tentatives")
# print("Nombre de points:",len(path_coords))
