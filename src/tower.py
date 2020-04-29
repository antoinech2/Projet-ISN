############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.3
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.3
#
# Description: Ce fichier contient l'objet qui gère les tours du jeu
# Il contient toutes les méthodes pour ...
############################################

############################################
#Importation des modules externes:
import pygame
############################################

############################################
# Définition de la class qui gère les tours:
class Tower(pygame.sprite.Sprite):

	@staticmethod
	def Init(path, box_pixel, ratio):
		"Initialisation des variables globales utiles pour la class Tower"
		Tower.path_coords = path
		Tower.box_size_pixel = box_pixel
		Tower.global_ratio = ratio

	def __init__(self):
		"Définition du constructeur avec toutes les caractéristiques des tours"
		super().__init__()
		self.image = pygame.Surface((50*Tower.global_ratio,50*Tower.global_ratio))
		self.image.fill(pygame.Color("red"))
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)

	def CursorPlace(self, position, group, rect_list):
		self.rect.center = (position[0],position[1])
		collide = pygame.sprite.spritecollide(self,group, False)
		if collide == [] and self.rect.collidelist(rect_list) == -1:
			self.image.fill(pygame.Color("green"))
		else:
			self.image.fill(pygame.Color("red"))

	def PlaceTower(self, position, group, rect_list):
		self.rect.center = (position[0],position[1])
		collide = pygame.sprite.spritecollide(self,group, False)
		if collide == [] and self.rect.collidelist(rect_list) == -1:
			self.image.fill(pygame.Color("blue"))
			return self
