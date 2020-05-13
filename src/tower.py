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
#Importation des modules internes:
import interfaces
############################################

############################################
# Définition de la class qui gère les tours:
class Tower(pygame.sprite.Sprite):
	LIFE_BAR_SIZE = (40,6)

	def __init__(self, game):
		"Définition du constructeur avec toutes les caractéristiques des tours"
		super().__init__()
		self.game = game
		self.image = pygame.Surface((50*self.game.global_ratio,50*self.game.global_ratio))
		self.image.fill(pygame.Color("red"))
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
		self.last_attack = time.time()

		self.range = int(2*self.game.global_ratio*self.game.box_size_pixel[0])
		self.attack_damage = 10
		self.attack_cooldown = 1
		self.attack_enemies = 1
		self.cost = 15
		self.shoot_max = 100
		self.shoot_remain = self.shoot_max

		self.life_bar = pygame.Surface(Tower.LIFE_BAR_SIZE)
		self.life_bar.fill(pygame.Color("green"))

	def CursorPlace(self, position):
		"Calcul de la couleur de la tour en fonction de sa position sur le terrain (disponible ou non)"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			if self.game.money <= self.cost:
				self.image.fill(pygame.Color("brown"))
				interfaces.RenderText("Fonds insuffisants", 15, "red", self.rect.center, self.game.screen)
			else:
				collide = pygame.sprite.spritecollide(self,self.game.all_towers, False)
				if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1:
					self.image.fill(pygame.Color("green"))
				else:
					self.image.fill(pygame.Color("red"))
		else:
			self.rect.center = (-100,-100)

	def Display(self):
		if self.game.money <= self.cost:
			interfaces.RenderText("Fonds insuffisants", 15, "red", (self.rect.center[0],self.rect.center[1]-10), self.game.screen)

	def PlaceTower(self, position):
		"Place la tour à l'endroit sélectionné au clic de la souris"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,self.game.all_towers, False)
			if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1 and self.game.money >= self.cost:
				self.game.money -= self.cost
				self.image.fill(pygame.Color("blue"))
				return self

	def DisplayRange(self):
		"Affiche le rayon d'action de la tour à l'écran"
		surface = pygame.Surface(self.game.screen_size, pygame.SRCALPHA)
		pygame.draw.circle(surface, pygame.Color(63, 127, 191, 128), self.rect.center, self.range)
		self.game.screen.blit(surface, (0,0))

	def DisplayLifeBar(self):
		"Affiche la barre de vie de l'ennemi à l'écran"
		self.game.screen.blit(self.life_bar, (self.rect.centerx-0.5*Tower.LIFE_BAR_SIZE[0],self.rect.y-6))

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
				self.shoot_remain -= 1
				if self.shoot_remain <= 0:
					self.game.all_towers.remove(self)
				else:
					self.life_bar.fill(pygame.Color("black"))
					life_percent = self.shoot_remain/self.shoot_max
					new_bar = pygame.Surface((Tower.LIFE_BAR_SIZE[0]*life_percent,Tower.LIFE_BAR_SIZE[1]))
					new_color = pygame.Color(int(255-(255*life_percent)),int(255*life_percent),0)
					new_bar.fill(new_color)
					self.life_bar.blit(new_bar, (0,0))
