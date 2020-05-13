############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.4.0-InDev
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 0.4.0-InDev
#
# Description: Ce fichier contient l'objet qui gère les tours du jeu
# Il contient toutes les méthodes pour ajouter et placer des tours sur la map
# ainsi que le tir des tours sur les ennemis.
############################################

############################################
#Importation des modules externes:
import pygame
import math
import time
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
		self.range = 3*Tower.global_ratio*Tower.box_size_pixel[0]
		self.attack_damage = 10
		self.attack_cooldown = 1
		self.attack_enemies = 1
		self.last_attack = time.time()

	def CursorPlace(self, position, group, rect_list, map_rect):
		"Calcul de la couleur de la tour en fonction de sa position sur le terrain (disponible ou non)"
		if map_rect.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,group, False)
			if collide == [] and self.rect.collidelist(rect_list) == -1:
				self.image.fill(pygame.Color("green"))
			else:
				self.image.fill(pygame.Color("red"))
		else:
			self.rect.center = (-100,-100)

	def PlaceTower(self, position, group, rect_list, map_rect):
		"Place la tour à l'endroit sélectionné au clic de la souris"
		if map_rect.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,group, False)
			if collide == [] and self.rect.collidelist(rect_list) == -1:
				self.image.fill(pygame.Color("blue"))
				return self

	def ShowRange(self, screen, screen_size):
		"Affiche le rayon d'action de la tour à l'écran"
		surface = pygame.Surface(screen_size, pygame.SRCALPHA)
		pygame.draw.circle(surface, pygame.Color(63, 127, 191, 128), self.rect.center, self.range)
		screen.blit(surface, (0,0))

	def Shot(self, all_enemies):
		"Trouve l'ennemi le plus proche pour lui faire des dègâts"
		if self.last_attack + self.attack_cooldown <= time.time():
			nearest_distance = 999999
			for current_enemy in all_enemies:
				distance = math.sqrt((self.rect.center[0] - current_enemy.rect.center[0])**2 + (self.rect.center[1] - current_enemy.rect.center[1])**2)
				if distance < self.range :
					if distance < nearest_distance:
						nearest_distance = distance
						nearest_ennemy = current_enemy
			if nearest_distance != 999999:
				nearest_ennemy.TakeDamage(self.attack_damage)
				self.last_attack = time.time()
