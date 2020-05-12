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

def RenderRightGUI(screen_size, game_health):
	"Affichage de l'interface latérale droite"
	gui_size = (0.2*screen_size[0],screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("Vies:"+str(game_health), 20, "green", (gui_size[0]-50, 20), gui)
	return gui

def RenderText(texte, taille, color, coords, surface, centered = True):
	"Affiche un texte en forme sur une surface"
	text = pygame.font.Font("../res/fonts/Righteous-Regular.ttf", taille).render(texte, True, pygame.Color(color))
	rect = text.get_rect()
	if centered:
		rect.center = coords
	surface.blit(text,rect)
