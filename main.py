
############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.1
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.1
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
############################################

############################################
#Définition des constantes générales du jeu:
screen_size = (1500,1000)
background_color = pygame.Color("red")
map_size = (15,15)
############################################

############################################
#Définition de la fonction principale:
def __main__():
	"Fonction principale"
	pygame.init() #Démarrage de Python

	#Initialisation de la fenêtre
	screen = pygame.display.set_mode(screen_size)
	pygame.display.set_caption("Tower Defense v0.1")

	is_game_running = True

	path_coords = map_generator.CalculateNewPath(map_size)
	#Boucle principale
	while is_game_running:
		screen.fill(background_color)
		pygame.display.update()

	pygame.quit() #Arrêt de pygame lorsque on sort de la boucle
############################################

__main__()
