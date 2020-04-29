############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.3
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.3
#
# Description: Ce fichier contient le programme principal qui gère
# la création de la fenêtre et la gestion de la boucle principale
# Il appelle les fonctions pour afficher les éléments à l'écran,
# ou analyser les évènements utilisateurs.
############################################

############################################
#Importation des modules externes:
import pygame
############################################

############################################
#Importation des modules internes:
import map_generator
import map_drawing
import enemy
import tower
import time
############################################

############################################
#Définition de la fonction principale:
def __main__():
	"Fonction principale"

	############################################
	#Définition des constantes générales du jeu:
	SCREEN_FORMAT = 9/16
	DEFAULT_SCREEN_SIZE = (992,558)
	MIN_SCREEN_SIZE = (750,422)
	MAP_SIZE = (16,9)

	TICK_TIME = 0.01 #Temps d'attente entre deux ticks en secondes
	############################################

	pygame.init() #Démarrage de pygame

	#Initialisation de la fenêtre
	screen_size = DEFAULT_SCREEN_SIZE
	screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)
	pygame.display.set_caption("Tower Defense v0.3")

	#Initialisation du jeu
	is_game_running = True
	current_tick = 0

	#Génération du chemin aléatoire
	path_coords = map_generator.CalculateNewPath(MAP_SIZE)
	#Génération graphique du rendu de la carte
	map_surface, box_size_pixel, map_rect_list = map_drawing.CreateMapSurface(MAP_SIZE,path_coords, screen_size)
	#Initialisation des ennemis
	enemy.Enemy.Init(path_coords, box_size_pixel, 1)
	all_enemies = pygame.sprite.Group()
	all_enemies.add(enemy.Enemy())
	#Initialisation des tours
	tower.Tower.Init(path_coords, box_size_pixel, 1)
	all_towers = pygame.sprite.Group()
	placing_tower = pygame.sprite.GroupSingle()

	#Boucle principale
	while is_game_running:
		current_tick += 1
		time.sleep(TICK_TIME)

		#EVENTS
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				is_game_running = False
			elif event.type == pygame.VIDEORESIZE:
				#Nouveau: event.w,event.h
				#Ancien : screen_size = (992,558)
				diff = (abs(event.w-screen_size[0]),abs(event.h-screen_size[1]))
				if diff[0] > diff[1]:
					w = max(MIN_SCREEN_SIZE[0],event.w)
					new_width, new_height = w, int(w*SCREEN_FORMAT)
				else:
					h = max(MIN_SCREEN_SIZE[1],event.h)
					new_width, new_height = int(h/SCREEN_FORMAT), h

				changed_ratio = new_width/screen_size[0]
				global_ratio = new_width/DEFAULT_SCREEN_SIZE[0]
				pygame.display.set_mode((new_width,new_height), pygame.RESIZABLE)
				screen_size = (new_width, new_height)
				map_surface, box_size_pixel = map_drawing.ResizeMapSurface(MAP_SIZE, screen_size, map_surface)
				enemy.Enemy.Init(path_coords, box_size_pixel, global_ratio)
				for current_enemy in all_enemies:
					current_enemy.UpdatePosition(changed_ratio)
					current_enemy.NewDestination()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_t:
					placing_tower.add(tower.Tower())
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if placing_tower.sprite != None:
					new_tower = placing_tower.sprite.PlaceTower(event.pos, all_towers, map_rect_list)
					if new_tower:
						all_towers.add(new_tower)
						placing_tower.empty()

		#CALCULS
		if current_tick%100 == 0:
			all_enemies.add(enemy.Enemy())
		for current_enemy in all_enemies:
			#current_enemy.TakeDamage(1)
			if current_enemy.HasFinished():
				all_enemies.remove(current_enemy)
			else:
				current_enemy.Move()
		for current_tower in placing_tower:
			current_tower.CursorPlace(pygame.mouse.get_pos(),all_towers, map_rect_list)

		#AFFICHAGE
		screen.blit(map_surface,(0,0))
		placing_tower.draw(screen)
		all_towers.draw(screen)
		all_enemies.draw(screen)
		for current_enemy in all_enemies:
			current_enemy.DisplayLifeBar(screen)

		#Rafraîchissement de l'écran
		pygame.display.flip()

	pygame.quit() #Arrêt de pygame lorsque on sort de la boucle
############################################

__main__()
