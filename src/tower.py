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

	def __init__(self, game):
		"Définition du constructeur avec toutes les caractéristiques des tours"
		super().__init__()
		self.game = game
		self.image = pygame.Surface((50*self.game.global_ratio,50*self.game.global_ratio))
		self.image.fill(pygame.Color("red"))
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
		self.last_attack = time.time()

		self.range = int(3*self.game.global_ratio*self.game.box_size_pixel[0])
		self.attack_damage = 10
		self.attack_cooldown = 1
		self.attack_enemies = 1
		self.cost = 15
		self.shoot_limit = 100

	def CursorPlace(self, position):
		"Calcul de la couleur de la tour en fonction de sa position sur le terrain (disponible ou non)"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,self.game.all_towers, False)
			if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1 and self.game.money >= self.cost:
				self.image.fill(pygame.Color("green"))
			else:
				self.image.fill(pygame.Color("red"))
		else:
			self.rect.center = (-100,-100)

	def PlaceTower(self, position):
		"Place la tour à l'endroit sélectionné au clic de la souris"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,self.game.all_towers, False)
			if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1 and self.game.money >= self.cost:
				self.game.money -= self.cost
				self.image.fill(pygame.Color("blue"))
				return self

	def ShowRange(self):
		"Affiche le rayon d'action de la tour à l'écran"
		surface = pygame.Surface(self.game.screen_size, pygame.SRCALPHA)
		pygame.draw.circle(surface, pygame.Color(63, 127, 191, 128), self.rect.center, self.range)
		self.game.screen.blit(surface, (0,0))

	def Shot(self):
		"Trouve l'ennemi le plus proche pour lui faire des dégâts"
		if self.last_attack + self.attack_cooldown <= time.time():
			nearest_distance = 999999
			for current_enemy in self.game.all_enemies:
				distance = math.sqrt((self.rect.center[0] - current_enemy.rect.center[0])**2 + (self.rect.center[1] - current_enemy.rect.center[1])**2)
				if distance < self.range :
					if distance < nearest_distance:
						nearest_distance = distance
						nearest_ennemy = current_enemy
			if nearest_distance != 999999:
				nearest_ennemy.TakeDamage(self.attack_damage)
				self.last_attack = time.time()
				self.shoot_limit -= 1
				if self.shoot_limit <= 0:
					self.game.all_towers.remove(self)
