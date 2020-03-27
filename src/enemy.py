
import pygame
import math
import random

#TODO: remplacer les variables globales par les varibles de Class

def Init(path, box_pixel, ratio):
	global path_coords, box_size_pixel, global_ratio
	path_coords = path
	box_size_pixel = box_pixel
	global_ratio = ratio

class Enemy(pygame.sprite.Sprite):
	life_bar_size = (25,4)
	def __init__(self):
		super().__init__()
		self.max_health = 100
		self.current_health = self.max_health
		self.resistance = 0.95
		self.speed = 1.5*global_ratio
		self.image = pygame.Surface((30*global_ratio,30*global_ratio))
		self.image.fill(pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		self.rect = self.image.get_rect()
		self.offset = (0.5*(1+self.rect.width/box_size_pixel[0]),0.5*(1+self.rect.height/box_size_pixel[1]))
		self.coords = (box_size_pixel[0]*(path_coords[0][0]-self.offset[0]),box_size_pixel[1]*(path_coords[0][1]-self.offset[1]))
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		self.current_case_number = 0
		self.position_precision = 15*global_ratio
		self.destination_offset = 0.15

		self.life_bar = pygame.Surface(Enemy.life_bar_size)
		self.life_bar.fill(pygame.Color(0, 255, 0))

		self.has_finished = False
		self.NewDestination()
	def Move(self):
		self.coords = (self.coords[0] + self.avance[0], self.coords[1] + self.avance[1])
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		if math.sqrt((self.coords[0]-self.coords_arrivee[0])**2+(self.coords[1]-self.coords_arrivee[1])**2) < self.position_precision:
			if self.current_case_number >= len(path_coords)-2:
				self.EndPath()
			else:
				self.current_case_number += 1
				self.NewDestination()
	def NewDestination(self):
		coords_depart = (self.rect.x, self.rect.y)
		self.coords_arrivee = (box_size_pixel[0]*(path_coords[self.current_case_number+1][0]-self.offset[0]+random.uniform(-self.destination_offset,self.destination_offset)) , box_size_pixel[1]*(path_coords[self.current_case_number+1][1]-self.offset[1]+random.uniform(-self.destination_offset,self.destination_offset)))
		direction_angle = math.atan2(self.coords_arrivee[1]-coords_depart[1], self.coords_arrivee[0]-coords_depart[0])
		self.avance = (math.cos(direction_angle)*self.speed, math.sin(direction_angle)*self.speed)
	def UpdatePosition(self, ratio):
		self.image = pygame.transform.scale(self.image,(int(self.rect.w*ratio),int(self.rect.h*ratio)))
		self.rect = self.image.get_rect()
		self.coords = (self.coords[0]*ratio,self.coords[1]*ratio)
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		self.speed *= ratio
	def EndPath(self):
		self.has_finished = True
	def HasFinished(self):
		return self.has_finished
	def DisplayLifeBar(self, dest):
		dest.blit(self.life_bar, (self.rect.centerx-0.5*Enemy.life_bar_size[0],self.rect.y-7))
	def TakeDamage(self, damage):
		total_damage = self.resistance * damage
		self.current_health -= total_damage
		if self.current_health <= 0:
			self.Death()
		else:
			self.life_bar.fill(pygame.Color("black"))
			life_percent = self.current_health/self.max_health
			new_bar = pygame.Surface((Enemy.life_bar_size[0]*life_percent,Enemy.life_bar_size[1]))
			new_color = pygame.Color(int(255-(255*life_percent)),int(255*life_percent),0)
			new_bar.fill(new_color)
			self.life_bar.blit(new_bar, (0,0))
	def Death(self):
		self.has_finished = True
