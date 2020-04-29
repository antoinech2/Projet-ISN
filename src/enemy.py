############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.3
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: InDev 0.3
#
# Description: Ce fichier contient l'objet qui gère les ennemis du jeu
# Il contient toutes les méthodes pour le faire appairaitre, disparaitre
# prendre des dégâts, afficher la barre de vie, etc...
############################################

############################################
#Importation des modules externes:
import pygame
import math
import random
############################################

############################################
# Définition de la class qui gère les ennemis:
class Enemy(pygame.sprite.Sprite):
	"Définition de la class Ennemis"
	#Définition des constantes globales à la class
	LIFE_BAR_SIZE = (25,4)

	@staticmethod
	def Init(path, box_pixel, ratio):
		"Initialisation des variables globales utiles pour la class Enemy"
		Enemy.path_coords = path
		Enemy.box_size_pixel = box_pixel
		Enemy.global_ratio = ratio

	def __init__(self):
		"Constructeur du nouvel objet ennemi avec un lot de caractéristiques"
		super().__init__()
		self.max_health = 100
		self.current_health = self.max_health
		self.resistance = 0.9
		self.speed = 1.5*Enemy.global_ratio

		self.position_precision = 15*Enemy.global_ratio
		self.destination_offset = 0.15

		self.image = pygame.Surface((30*Enemy.global_ratio,30*Enemy.global_ratio))
		self.image.fill(pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		#self.image = pygame.image.load("../res/textures/ennemy/enemy.PNG")
		self.rect = self.image.get_rect()
		self.offset = (0.5*(1+self.rect.width/Enemy.box_size_pixel[0]),0.5*(1+self.rect.height/Enemy.box_size_pixel[1]))
		self.coords = (Enemy.box_size_pixel[0]*(Enemy.path_coords[0][0]-self.offset[0]),Enemy.box_size_pixel[1]*(Enemy.path_coords[0][1]-self.offset[1]))
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		self.current_case_number = 0
		self.has_finished = False

		self.life_bar = pygame.Surface(Enemy.LIFE_BAR_SIZE)
		self.life_bar.fill(pygame.Color("green"))

		self.NewDestination()
	def Move(self):
		"Méthode pour faire avancer l'ennemi de quelques pixels dans la bonne direction"
		self.coords = (self.coords[0] + self.avance[0], self.coords[1] + self.avance[1])
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		if math.sqrt((self.coords[0]-self.coords_arrivee[0])**2+(self.coords[1]-self.coords_arrivee[1])**2) < self.position_precision:
			if self.current_case_number >= len(Enemy.path_coords)-2:
				self.EndPath()
			else:
				self.current_case_number += 1
				self.NewDestination()
	def NewDestination(self):
		"Calcul de la nouvelle destination (angle) vers la prochaine case"
		coords_depart = (self.rect.x, self.rect.y)
		self.coords_arrivee = (Enemy.box_size_pixel[0]*(Enemy.path_coords[self.current_case_number+1][0]-self.offset[0]+random.uniform(-self.destination_offset,self.destination_offset)) , Enemy.box_size_pixel[1]*(Enemy.path_coords[self.current_case_number+1][1]-self.offset[1]+random.uniform(-self.destination_offset,self.destination_offset)))
		direction_angle = math.atan2(self.coords_arrivee[1]-coords_depart[1], self.coords_arrivee[0]-coords_depart[0])
		self.avance = (math.cos(direction_angle)*self.speed, math.sin(direction_angle)*self.speed)
	def UpdatePosition(self, ratio):
		"Méthode pour replacer correctement les ennemis après redimention de la fenêtre graphique"
		self.image = pygame.transform.scale(self.image,(int(self.rect.w*ratio),int(self.rect.h*ratio)))
		self.rect = self.image.get_rect()
		self.coords = (self.coords[0]*ratio,self.coords[1]*ratio)
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		self.speed *= ratio
	def EndPath(self):
		"Définit l'état de course de l'ennemi comme terminée"
		self.has_finished = True
	def HasFinished(self):
		"Retourne l'état de course de l'ennemi"
		return self.has_finished
	def GetHealth(self):
		"Retourne la vie restante de l'ennemi"
		return self.current_health
	def DisplayLifeBar(self, dest):
		"Affiche la barre de vie de l'ennemi à l'écran"
		dest.blit(self.life_bar, (self.rect.centerx-0.5*Enemy.LIFE_BAR_SIZE[0],self.rect.y-7))
	def TakeDamage(self, damage):
		"Fait prendre un certain nombre de dommage à l'ennemi"
		total_damage = self.resistance * damage
		self.current_health -= total_damage
		if self.current_health <= 0:
			self.Death()
		else:
			self.life_bar.fill(pygame.Color("black"))
			life_percent = self.current_health/self.max_health
			new_bar = pygame.Surface((Enemy.LIFE_BAR_SIZE[0]*life_percent,Enemy.LIFE_BAR_SIZE[1]))
			new_color = pygame.Color(int(255-(255*life_percent)),int(255*life_percent),0)
			new_bar.fill(new_color)
			self.life_bar.blit(new_bar, (0,0))
	def Death(self):
		"Fait mourir l'ennemi (plus de vie)"
		self.has_finished = True
