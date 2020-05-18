############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.4.0-InDev
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 0.4.0-InDev
#
# Description: Ce fichier contient les fonctions qui gèrent
# les interfaces latérales du jeu, les menu de début, fin et pause
# ainsi que l'affichage de textes à l'écran.
############################################

############################################
#Importation des modules externes:
import pygame
############################################

def RenderRightGUI(screen_size, game_health, game_money, number_tower, number_ennemis, number_kill, fps):
	"Affichage de l'interface latérale droite"
	gui_size = (0.2*screen_size[0],screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("FPS: "+str(fps), 10, "red", (gui_size[0]-30, 10), gui)
	RenderText("Vies: "+str(round(game_health, 1)), 20, "orange", (gui_size[0]-100, 20), gui)
	RenderText("Argent: "+str(round(game_money, 1)), 20, "orange", (gui_size[0]-100, 50), gui)
	RenderText("Nombre de tours: "+str(number_tower), 13, "brown", (gui_size[0]-100, 100), gui)
	RenderText("Nombre d'ennemis: "+str(number_ennemis), 13, "brown", (gui_size[0]-100, 130), gui)
	RenderText("Nombre d'ennemis vaincus: "+str(number_kill), 13, "brown", (gui_size[0]-100, 160), gui)
	return gui

def RenderBottomGUI(game):
	"Affichage de l'interface latérale droite"
	gui_size = (0.8*game.screen_size[0],0.2*game.screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	# RenderText("Nombre d'ennemis vaincus: "+str(number_kill), 13, "brown", (gui_size[0]-100, 160), gui)
	return gui

def ShowTowerStats(game, tower):
	gui_size = (0.8*game.screen_size[0],0.2*game.screen_size[1])
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
	gui_size = (0.8*game.screen_size[0],0.2*game.screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("Informations sur l'ennemi: ", 20, "red", (150, 20), gui)
	RenderText("Résistance: "+str(round(enemy.resistance,2)), 15, "black", (150, 40), gui)
	RenderText("Vitesse: "+str(round(enemy.speed,2)), 15, "black", (150, 60), gui)
	RenderText("Gain d'élimination: "+str(round(enemy.money_gain,1)), 15, "black", (150, 80), gui)
	#RenderText("Réduction de vie par tir: "+str(tower.shoot_reduction)+"±"+str(tower.random_shoot_reduction_range), 15, "black", (150, 100), gui)

	RenderText("Statistiques sur l'ennemi: ", 20, "red", (450, 20), gui)
	RenderText("Vie: "+str(round(enemy.current_health,1))+"/"+str(round(enemy.max_health,1))+" ("+str(round(enemy.current_health/enemy.max_health*100))+" %)", 15, "black", (450, 40), gui)
	RenderText("Position: "+str(enemy.current_case_number)+"/"+str(len(game.path_coords)-1), 15, "black", (450, 60), gui)
	#RenderText("Tirs totaux: "+str(tower.total_shoot), 15, "black", (450, 60), gui)
	#RenderText("Dêgats infligés: "+str(round(tower.total_damage,1)), 15, "black", (450, 80), gui)
	#RenderText("Ennemis éliminés: "+str(tower.total_kill), 15, "black", (450, 100), gui)
	return gui


def RenderText(texte, taille, color, coords, surface, centered = True):
	"Affiche un texte en forme sur une surface"
	# pygame.font.Font("../res/fonts/Righteous-Regular.ttf", taille)
	text = font[taille].render(texte, True, pygame.Color(color))
	rect = text.get_rect()
	if centered:
		rect.center = coords
	surface.blit(text,rect)

def InitFonts():
	global font
	pygame.font.init()
	font = []
	for number in range(100):
		font.append(pygame.font.Font("../res/fonts/Righteous-Regular.ttf", number))

InitFonts()
