############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
#
# Description: Ce fichier contient l'objet qui gère les tours et les projectiles du jeu
# Il contient toutes les méthodes pour ajouter et placer des tours sur la map
# ainsi que le tir des tours sur les ennemis.
############################################

############################################
#Importation des modules externes:
import pygame
import math
import time
import random
from sys import path
############################################

path.append("../res/data/")

############################################
#Importation des modules internes:
import interfaces
import tower_data
############################################

############################################
def InitTowers():
	Tower.images = []
	for tower in tower_data.towers:
		Tower.images.append(pygame.image.load(tower["image_path"]))

# Définition de la class qui gère les tours:
class Tower(pygame.sprite.Sprite):
	def __init__(self, game, tower_type):
		"Définition du constructeur avec toutes les caractéristiques des tours"
		super().__init__()
		#Global
		data = tower_data.towers[tower_type]
		self.game = game
		#self.image = pygame.Surface((50*self.game.global_ratio,50*self.game.global_ratio))
		#self.image.fill(pygame.Color("red"))
		self.image = pygame.transform.scale(Tower.images[tower_type], data["image_size"])  #pygame.image.load(data["image_path"])
		self.rect = self.image.get_rect()
		self.rect.center = (0,0)
		self.last_attack = time.time()

		#caractéristiques
		self.name = data["name"]
		self.range = int(data["range"]*self.game.global_ratio*self.game.box_size_pixel[0])
		self.radius = int(0.5*data["image_size"][0])
		self.attack_damage = data["attack_damage"][0]
		self.random_attack_damage_range = data["attack_damage"][1]
		self.attack_cooldown = data["attack_cooldown"][0]
		self.random_attack_cooldown_range = data["attack_cooldown"][1]
		self.attack_enemies = data["attack_enemies"][0]
		self.random_attack_enemies_range = data["attack_enemies"][1]
		self.cost = data["cost"]
		self.shoot_max = data["shoot_max"]
		self.shoot_reduction = data["shoot_reduction"][0]
		self.random_shoot_reduction_range = data["shoot_reduction"][1]
		self.shoot_remain = self.shoot_max
		self.projectile_speed = data["projectile_speed"][0]
		self.random_projectile_speed_range = data["projectile_speed"][1]

		#Statistiques
		self.total_shoot = 0
		self.total_damage = 0
		self.total_kill = 0

		#Barre de vie
		self.life_bar_range = data["life_bar_range"]
		self.life_bar = pygame.Surface((2*self.life_bar_range,2*self.life_bar_range), pygame.SRCALPHA)
		pygame.draw.ellipse(self.life_bar, pygame.Color("green"), self.life_bar.get_rect())

		#Couleur de position
		self.placement_color = pygame.Surface(data["image_size"], pygame.SRCALPHA)
		pygame.draw.circle(self.placement_color,pygame.Color("red"),self.placement_color.get_rect().center, self.radius)

	def CursorPlace(self, position):
		"Calcul de la couleur de la tour en fonction de sa position sur le terrain (disponible ou non)"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			if self.game.money <= self.cost:
				pygame.draw.circle(self.placement_color,pygame.Color(158, 101, 32, 50),self.placement_color.get_rect().center, self.radius)
				interfaces.RenderText("Fonds insuffisants", 15, "red", self.rect.center, self.game.screen)
			else:
				collide = pygame.sprite.spritecollide(self,self.game.all_towers, False, pygame.sprite.collide_circle)
				if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1:
					#pygame.draw.rect(self.image, pygame.Color(255,0,0,120), (0,0,self.rect.width, self.rect.height))
					pygame.draw.circle(self.placement_color,pygame.Color(0,255,0,50),self.placement_color.get_rect().center, self.radius)
				else:
					pygame.draw.circle(self.placement_color,pygame.Color(255,0,0,50),self.placement_color.get_rect().center, self.radius)
		else:
			self.rect.center = (-100,-100)

	def Display(self):
		self.game.screen.blit(self.placement_color, self.rect.topleft)
		if self.game.money <= self.cost:
			interfaces.RenderText("Fonds insuffisants", 15, "red", (self.rect.center[0],self.rect.center[1]-10), self.game.screen)

	def PlaceTower(self, position):
		"Place la tour à l'endroit sélectionné au clic de la souris"
		if self.game.map_surface.get_rect().collidepoint(position):
			self.rect.center = (position[0],position[1])
			collide = pygame.sprite.spritecollide(self,self.game.all_towers, False, pygame.sprite.collide_circle)
			if collide == [] and self.rect.collidelist(self.game.map_rect_list) == -1 and self.game.money >= self.cost:
				self.game.money -= self.cost
				#self.image.fill(pygame.Color("blue"))
				return self

	def DisplayRange(self):
		"Affiche le rayon d'action de la tour à l'écran"
		surface = pygame.Surface(self.game.screen_size, pygame.SRCALPHA)
		pygame.draw.circle(surface, pygame.Color(63, 127, 191, 128), self.rect.center, self.range)
		self.game.screen.blit(surface, (0,0))

	def DisplayLifeBar(self):
		"Affiche la barre de vie de l'ennemi à l'écran"
		self.game.screen.blit(self.life_bar, (self.rect.centerx-self.life_bar_range,self.rect.centery-self.life_bar_range))

	def Shot(self):
		"Trouve l'ennemi le plus proche pour lui faire des dégâts"
		if self.last_attack + self.attack_cooldown <= time.time():
			ennemies_distance = {}
			attack_enemies_bonus = random.randint(-self.random_attack_enemies_range,self.random_attack_enemies_range)
			for current_enemy in self.game.all_enemies:
				distance = math.sqrt((self.rect.center[0] - current_enemy.rect.center[0])**2 + (self.rect.center[1] - current_enemy.rect.center[1])**2)
				if distance < self.range :
					ennemies_distance[round(distance,1)] = current_enemy
			ennemies_attacked = 0
			for index in sorted(ennemies_distance.keys()):
				if ennemies_attacked < self.attack_enemies + attack_enemies_bonus:
					ennemies_attacked += 1
					self.game.all_projectiles.add(Projectile(self, ennemies_distance[index]))
					#ennemies_distance[index].TakeDamage(self.attack_damage + random.uniform(-self.random_attack_damage_range, self.random_attack_damage_range), self)
					self.last_attack = time.time() + random.uniform(-self.random_attack_cooldown_range,self.random_attack_cooldown_range)
					self.total_shoot += 1
					if self.shoot_remain <= 0:
						self.game.all_towers.remove(self)
					else:
						pygame.draw.ellipse(self.life_bar, pygame.Color("black"), self.life_bar.get_rect())
						life_percent = self.shoot_remain/self.shoot_max
						new_color = pygame.Color(int(255-(255*life_percent)),int(255*life_percent),0)
						pygame.draw.arc(self.life_bar, new_color, self.life_bar.get_rect(), math.pi/2, life_percent*2*math.pi+math.pi/2, 20)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+3, self.life_bar.get_rect().top+1, self.life_bar_range*2-4, self.life_bar_range*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+1, self.life_bar.get_rect().top+3, self.life_bar_range*2-4, self.life_bar_range*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+3, self.life_bar.get_rect().top+3, self.life_bar_range*2-4, self.life_bar_range*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
						pygame.draw.arc(self.life_bar, new_color, pygame.Rect(self.life_bar.get_rect().left+1, self.life_bar.get_rect().top+1, self.life_bar_range*2-4, self.life_bar_range*2), math.pi/2, life_percent*2*math.pi+math.pi/2, 17)
				else:
					break
			if ennemies_attacked > 0:
				self.shoot_remain -= self.shoot_reduction + random.uniform(-self.random_shoot_reduction_range,self.random_shoot_reduction_range)

class Projectile(pygame.sprite.Sprite):
	def __init__(self, tower, target):
		"Définition du constructeur avec toutes les caractéristiques des projectiles"
		super().__init__()
		#Global
		self.tower = tower
		self.target = target

		self.image = pygame.Surface((10*self.tower.game.global_ratio,5*self.tower.game.global_ratio))
		self.image.fill(pygame.Color("red"))
		self.rect = self.image.get_rect()
		self.coords = [self.tower.rect.centerx, self.tower.rect.centery]
		self.rect.center = self.coords

		#caractéristiques
		self.speed = self.tower.projectile_speed + random.uniform(-self.tower.random_projectile_speed_range, self.tower.random_projectile_speed_range)

	def Move(self):
		"Fait avancer le projectile dans la direction de sa cible"
		angle = math.atan2(self.target.rect.centery - self.rect.centery, self.target.rect.centerx - self.rect.centerx)
		self.coords[0] += self.speed*math.cos(angle)
		self.coords[1] += self.speed*math.sin(angle)
		self.rect[0] = self.coords[0]
		self.rect[1] = self.coords[1]
		if math.hypot(self.target.rect.centerx - self.rect.centerx, self.target.rect.centery - self.rect.centery) < 0.5*self.target.rect.width:
			self.target.TakeDamage(self.tower.attack_damage + random.uniform(-self.tower.random_attack_damage_range, self.tower.random_attack_damage_range), self.tower)
			self.tower.game.all_projectiles.remove(self)
