############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.1
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.2
#
# Script principal d'affichage graphique de la map
#
# Description: Ce fichier va se charger d'afficher la map à l'écran grâce notamment
# à la génération du chemin grâce au fichier "map_generator" qui se charge de choisir
# les coordonnées, des cases correspondant au chemin, dans un quadrillage de la fenetre de jeu.
############################################

############################################
# Importation des modules:
import pygame
import math
import random
############################################
# Importation des images :

img_chemin = pygame.image.load('../res/textures/map/chemin.png')
img_herbe = pygame.image.load('../res/textures/map/herbe.png')
img_herbev2 = pygame.image.load('../res/textures/map/herbev2.png')
img_plante = pygame.image.load('../res/textures/map/plante.png')
img_arbre = pygame.image.load('../res/textures/map/arbre.png')
############################################
# Définition des fonctions locales:
def CreateMapSurface(map_size,path_coords, screen_size):
	"Fonction de création de la surface pygame représentant la map"
	# Définition des constantes de fonction:
	map_size_pixel = (0.8*screen_size[0],0.8*screen_size[1])
	box_size_pixel = (math.floor(map_size_pixel[0]/map_size[0]),math.floor(map_size_pixel[1]/map_size[1]))
	img_che = pygame.transform.scale(img_chemin,(box_size_pixel[0],box_size_pixel[1]))
	img_herb = pygame.transform.scale(img_herbe,(box_size_pixel[0],box_size_pixel[1]))
	img_herbv2 = pygame.transform.scale(img_herbev2,(box_size_pixel[0],box_size_pixel[1]))
	img_plant = pygame.transform.scale(img_plante,(box_size_pixel[0],box_size_pixel[1]))
	img_arbr = pygame.transform.scale(img_arbre,(box_size_pixel[0],box_size_pixel[1]))
	############################################
	map_surface = pygame.Surface(map_size_pixel)
	for column in range (1,map_size[0]+1):
		for row in range (1,map_size[1]+1):
			current_box = pygame.Surface(box_size_pixel)
			if (column,row) in path_coords:
				image = img_che
			else :
				image = random.choice([img_herbv2,img_herbv2,img_herbv2,img_herbv2,img_herbv2,img_plant,img_arbr])
			map_surface.blit(image,((column-1)*box_size_pixel[0],(row-1)*box_size_pixel[1]))
	return map_surface, box_size_pixel

def ResizeMapSurface(map_size, screen_size, map_surface):
	map_size_pixel = (0.8*screen_size[0],0.8*screen_size[1])
	box_size_pixel = (math.floor(map_size_pixel[0]/map_size[0]),math.floor(map_size_pixel[1]/map_size[1]))
	map_surface = pygame.transform.scale(map_surface,(int(map_size_pixel[0]),int(map_size_pixel[1])))
	return map_surface, box_size_pixel
