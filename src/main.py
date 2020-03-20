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
import time
############################################

############################################
#Définition des constantes générales du jeu:
screen_format = 9/16
default_screen_size = (992,558)
screen_size = default_screen_size
min_screen_size = (750,422)
map_size = (16,9)
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
	map_surface, box_size_pixel = map_drawing.CreateMapSurface(map_size,path_coords, screen_size)
	enemy.Init(path_coords, box_size_pixel, 1)
	all_enemies = pygame.sprite.Group()
	all_enemies.add(enemy.Enemy())
	current_tick = 0
	#Boucle principale
	while is_game_running:
		current_tick += 1
		time.sleep(0.01)

		#EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_game_running = False
			elif event.type == pygame.VIDEORESIZE:
				#Nouveau: event.w,event.h
				#Ancien : screen_size = (992,558)
				diff = (abs(event.w-screen_size[0]),abs(event.h-screen_size[1]))
				if diff[0] > diff[1]:
					w = max(min_screen_size[0],event.w)
					new_width, new_height = w, int(w*screen_format)
				else:
					h = max(min_screen_size[1],event.h)
					new_width, new_height = int(h/screen_format), h

				changed_ratio = new_width/screen_size[0]
				global_ratio = new_width/default_screen_size[0]
				pygame.display.set_mode((new_width,new_height), pygame.RESIZABLE)
				screen_size = (new_width, new_height)
				map_surface, box_size_pixel = map_drawing.ResizeMapSurface(map_size, screen_size, map_surface)
				enemy.Init(path_coords, box_size_pixel, global_ratio)
				for current_enemy in all_enemies:
					current_enemy.UpdatePosition(changed_ratio)
					current_enemy.NewDestination()

		#CALCULS
		if current_tick%100 == 0:
			all_enemies.add(enemy.Enemy())
		for current_enemy in all_enemies:
			if current_enemy.HasFinished():
				all_enemies.remove(current_enemy)
			else:
				current_enemy.Move()

		#AFFICHAGE
		screen.blit(map_surface,(0,0))
		all_enemies.draw(screen)
		pygame.display.flip()
	pygame.quit() #Arrêt de pygame lorsque on sort de la boucle
############################################

__main__()
