############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
#
# Description: Ce fichier contient les fonctions qui gèrent
# les interfaces latérales du jeu, les menu de début, fin et pause
# ainsi que l'affichage de textes à l'écran.
############################################

############################################
#Importation des modules externes:
import pygame
import time
from sys import path
############################################

path.append("../res/data/")

############################################
#Importation des modules internes:
import tower_data
import tower
############################################

def RenderRightGUI(game):
	"Affichage de l'interface latérale droite"
	gui_size = (0.2*game.screen_size[0],game.screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("FPS: "+str(game.last_fps), 10, "red", (gui_size[0]-30, gui_size[1]-10), gui)
	RenderText("Vies: "+str(round(game.health, 1)), 20, "orange", (gui_size[0]-100, 20), gui)
	RenderText("Argent: "+str(round(game.money, 1)), 20, "orange", (gui_size[0]-100, 50), gui)
	RenderText("Nombre de tours: "+str(len(game.all_towers)), 13, "brown", (gui_size[0]-100, 100), gui)
	RenderText("Nombre d'ennemis: "+str(len(game.all_enemies)), 13, "brown", (gui_size[0]-100, 130), gui)
	RenderText("Nombre d'ennemis vaincus: "+str(game.ennemies_killed), 13, "brown", (gui_size[0]-100, 160), gui)
	RenderText("Vague "+str(game.vague.current_vague+1), 25, "blue", (gui_size[0]-100, 200), gui)
	RenderText("Nombre d'ennemis: "+ str(game.vague.current_spawned) + " / " + str(game.vague.total_enemies), 15, "blue", (gui_size[0]-100, 230), gui)
	RenderText("Ennemis restants: "+str(game.vague.total_enemies-game.vague.current_spawned+len(game.all_enemies)), 15, "blue", (gui_size[0]-100, 250), gui)
	delta = int(game.vague.time_after_vague + (game.vague.total_enemies-game.vague.current_spawned)*game.vague.time_between_enemies + (game.vague.time_between_enemies-(time.time()-game.vague.last_spawn_time)))
	RenderText("Prochaine vague dans ", 15, "blue", (gui_size[0]-100, 270), gui)
	RenderText("{:0>2d}".format(int(delta/60)) + ":" + "{:0>2d}".format(delta%60), 20, "blue", (gui_size[0]-100, 290), gui)

	index = 0
	for current_tower in tower_data.towers:
		pygame.draw.rect(gui, pygame.Color(117, 117, 117), pygame.Rect(5+65*(index%3),320+65*int(index/3),55,55), 3)
		gui.blit(pygame.transform.scale(tower.Tower.images[index],(45,45)), (10+65*(index%3),325+65*int(index/3)))
		index += 1
	return gui

def CheckMouseCollision(game):
	gui_size_x = 0.8*game.screen_size[0]
	index = 0
	for current_tower in tower_data.towers:
		rect = pygame.Rect(gui_size_x+5+65*(index%3),320+65*int(index/3),55,55)
		if rect.collidepoint(pygame.mouse.get_pos()):
			return index
		index += 1

def ShowPlacementTowerStats(game, tower_type):
	"Affichage des informations et statistiques de la tour sélectionnée dans le menu latéral"
	gui_size = (0.8*game.screen_size[0]+1,0.2*game.screen_size[1]+1)
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	tower_info = tower_data.towers[tower_type]
	RenderText("Informations sur la tour: " + str(tower_info["name"]), 20, "red", (275, 20), gui)
	RenderText("Taille: "+str(round(tower_info["image_size"][0]/game.box_size_pixel[0],2))+" x "+str(round(tower_info["image_size"][1]/game.box_size_pixel[1],2)), 15, "black", (150, 40), gui)
	RenderText("Dégâts: "+str(tower_info["attack_damage"][0])+"±"+str(tower_info["attack_damage"][1]), 15, "black", (150, 60), gui)
	RenderText("Délai d'attaque: "+str(tower_info["attack_cooldown"][0])+"±"+str(tower_info["attack_cooldown"][1])+" sec.", 15, "black", (150, 80), gui)
	RenderText("Attaques simultanées: "+str(tower_info["attack_enemies"][0])+"±"+str(tower_info["attack_enemies"][1]), 15, "black", (150, 100), gui)
	RenderText("Réduction de vie par tir: "+str(tower_info["shoot_reduction"][0])+"±"+str(tower_info["shoot_reduction"][1]), 15, "black", (400, 40), gui)
	RenderText("Vie: "+str(tower_info["shoot_max"]), 15, "black", (400, 60), gui)
	RenderText("Vitesse des projectiles: "+str(tower_info["projectile_speed"][0])+"±"+str(tower_info["projectile_speed"][1]), 15, "black", (400, 80), gui)
	RenderText("Rayon d'action: "+str(tower_info["range"]), 15, "black", (400, 100), gui)
	return gui


def RenderBottomGUI(game):
	"Affichage de l'interface latérale basse"
	gui_size = (0.8*game.screen_size[0]+1,0.2*game.screen_size[1]+1)
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	return gui

def ShowTowerStats(game, tower):
	"Affichage des informations et statistiques de la tour pointée"
	gui_size = (0.8*game.screen_size[0]+1,0.2*game.screen_size[1]+1)
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("Informations sur la tour: ", 20, "red", (150, 20), gui)
	RenderText("Dégâts: "+str(tower.attack_damage)+"±"+str(tower.random_attack_damage_range), 15, "black", (150, 40), gui)
	RenderText("Délai d'attaque: "+str(tower.attack_cooldown)+"±"+str(tower.random_attack_cooldown_range)+" sec.", 15, "black", (150, 60), gui)
	RenderText("Attaques simultanées: "+str(tower.attack_enemies)+"±"+str(tower.random_attack_enemies_range), 15, "black", (150, 80), gui)
	RenderText("Réduction de vie par tir: "+str(tower.shoot_reduction)+"±"+str(tower.random_shoot_reduction_range), 15, "black", (150, 100), gui)

	RenderText("Statistiques sur la tour: ", 20, "red", (450, 20), gui)
	RenderText("Vies: "+str(round(tower.shoot_remain,1))+"/"+str(tower.shoot_max)+" ("+str(round(tower.shoot_remain/tower.shoot_max*100))+" %)", 15, "black", (450, 40), gui)
	RenderText("Tirs totaux: "+str(tower.total_shoot), 15, "black", (450, 60), gui)
	RenderText("Dêgats infligés: "+str(round(tower.total_damage,1)), 15, "black", (450, 80), gui)
	RenderText("Ennemis éliminés: "+str(tower.total_kill), 15, "black", (450, 100), gui)
	return gui

def ShowEnnemyStats(game, enemy):
	"Affichage des informations et statistiques de l'ennemi pointé"
	gui_size = (0.8*game.screen_size[0]+1,0.2*game.screen_size[1]+1)
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("Informations sur l'ennemi: ", 20, "red", (150, 20), gui)
	RenderText("Résistance: "+str(round(enemy.resistance,2)), 15, "black", (150, 40), gui)
	RenderText("Vitesse: "+str(round(enemy.speed,2)), 15, "black", (150, 60), gui)
	RenderText("Gain d'élimination: "+str(round(enemy.money_gain,1)), 15, "black", (150, 80), gui)
	RenderText("Statistiques sur l'ennemi: ", 20, "red", (450, 20), gui)
	RenderText("Vie: "+str(round(enemy.current_health,1))+"/"+str(round(enemy.max_health,1))+" ("+str(round(enemy.current_health/enemy.max_health*100))+" %)", 15, "black", (450, 40), gui)
	RenderText("Position: "+str(enemy.current_case_number)+"/"+str(len(game.path_coords)-1), 15, "black", (450, 60), gui)
	return gui


def RenderText(texte, taille, color, coords, surface, centered = True):
	"Affiche un texte en forme sur une surface"
	text = font[taille].render(texte, True, pygame.Color(color))
	rect = text.get_rect()
	if centered:
		rect.center = coords
	surface.blit(text,rect)

def InitFonts():
	"Initialisation des polices"
	global font
	pygame.font.init()
	font = []
	for number in range(100):
		font.append(pygame.font.Font("../res/fonts/Righteous-Regular.ttf", number))

InitFonts()
