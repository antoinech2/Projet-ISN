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
	LIFE_BAR_RANGE = 30

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
		self.attack_damage = 20
		self.attack_cooldown = 1
		self.attack_enemies = 1
		self.cost = 15
		self.shoot_max = 100
		self.shoot_remain = self.shoot_max

		self.total_shoot = 0
		self.total_damage = 0
		self.total_kill = 0

		self.life_bar = pygame.Surface((2*Tower.LIFE_BAR_RANGE,2*Tower.LIFE_BAR_RANGE), pygame.SRCALPHA)
		pygame.draw.ellipse(self.life_bar, pygame.Color("green"), self.life_bar.get_rect())

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
		self.game.screen.blit(self.life_bar, (self.rect.centerx-Tower.LIFE_BAR_RANGE,self.rect.centery-Tower.LIFE_BAR_RANGE))

	def Shot(self):
		"Trouve l'ennemi le plus proche pour lui faire des dégâts"
		if self.last_attack + self.attack_cooldown <= time.time():
			ennemies_distance = {}
			for current_enemy in self.game.all_enemies:
				distance = math.sqrt((self.rect.center[0] - current_enemy.rect.center[0])**2 + (self.rect.center[1] - current_enemy.rect.center[1])**2)
				if distance < self.range :
					ennemies_distance[round(distance,1)] = current_enemy
			ennemies_attacked = 0
			for index in sorted(ennemies_distance.keys()):
				if ennemies_attacked < self.attack_enemies:
					ennemies_attacked += 1
					ennemies_distance[index].TakeDamage(self.attack_damage, self)
					self.last_attack = time.time()
					self.total_shoot += 1
					if self.shoot_remain <= 0:
						self.game.all_towers.remove(self)
					else:
						pygame.draw.ellipse(self.life_bar, pygame.Color("black"), self.life_bar.get_rect())
						life_percent = self.shoot_remain/self.shoot_max
						new_color = pygame.Color(int(255-(255*life_percent)),int(255*life_percent),0)
						pygame.draw.arc(self.life_bar, new_color, self.life_bar.get_rect(), math.pi/2, life_percent*2*math.pi+math.pi/2, 20)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+3, self.life_bar.get_rect().top+1, Tower.LIFE_BAR_RANGE*2-4, Tower.LIFE_BAR_RANGE*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+1, self.life_bar.get_rect().top+3, Tower.LIFE_BAR_RANGE*2-4, Tower.LIFE_BAR_RANGE*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+3, self.life_bar.get_rect().top+3, Tower.LIFE_BAR_RANGE*2-4, Tower.LIFE_BAR_RANGE*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+1, self.life_bar.get_rect().top+1, Tower.LIFE_BAR_RANGE*2-4, Tower.LIFE_BAR_RANGE*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
				else:
					break
			if ennemies_attacked > 0:
				self.shoot_remain -= 1
