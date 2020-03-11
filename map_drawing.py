############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.1
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.1
#
# Script principal d'affichage graphique de la map
#
# Description: Ce fichier va se charger d'afficher la map à l'écran grâce notamment
#à la génération du chemin grâce au fichier "map_generator" qui se charge de choisir
#les coordonnées, des cases correspondant au chemin, dans un quadrillage de la fenetre de jeu .
############################################

############################################
#Importation des modules:
import pygame
import math

############################################
#definition des constantes :
map_size_pixel=(825,525)

############################################
#definition de la fonction d'affichage :
def ShowMap (map_size,path_coords):
    box_size_pixel=(math.floor(map_size_pixel[0]/map_size[0]),math.floor(map_size_pixel[1]/map_size[1]))
    map_surface=pygame.Surface(map_size_pixel)
    for column in range (1,map_size[0]+1):
        for row in range (1,map_size[1]+1):
            current_box=pygame.Surface(box_size_pixel)
            if (column,row) in path_coords:
                current_box.fill((200,0,0))
            else :
                current_box.fill((255,255,255))
            map_surface.blit(current_box,((column-1)*box_size_pixel[0],(row-1)*box_size_pixel[1]))
    return map_surface
