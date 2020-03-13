############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.1
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.2
#
# Description: Ce fichier contient le programme principal qui gère
# la création de la fenêtre et la gestion de la boucle principale
# Il appelle les fonctions pour afficher les éléments à l'écran,
# ou analyser les évènements utilisateurs.
############################################

############################################
#Importation des modules:
import pygame
############################################

############################################
#Importation des modules:
import map_generator
import map_drawing
import enemy
############################################

############################################
#Définition des constantes générales du jeu:
screen_size = (900,600)
map_size = (10,10)
############################################

############################################
#Définition de la fonction principale:
def __main__():
	global screen_size, map_size
	"Fonction principale"
	pygame.init() #Démarrage de Python

	#Initialisation de la fenêtre
	screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
	pygame.display.set_caption("Tower Defense v0.2")

	is_game_running = True

	path_coords = map_generator.CalculateNewPath(map_size)
	map_surface = map_drawing.CreateMapSurface(map_size,path_coords, screen_size)
	all_enemies = pygame.sprite.Group()
	all_enemies.add(enemy.enemy())

	#Boucle principale
	while is_game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_game_running = False
			elif event.type == pygame.VIDEORESIZE:
				pygame.display.set_mode(event.size, pygame.RESIZABLE)
				screen_size = (event.w, event.h)
				map_surface = map_drawing.CreateMapSurface(map_size,path_coords, screen_size)
		screen.blit(map_surface,(0,0))
		all_enemies.draw(screen)
		pygame.display.update()

	pygame.quit() #Arrêt de pygame lorsque on sort de la boucle
############################################

__main__()
