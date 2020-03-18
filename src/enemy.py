
import pygame
import math
import random

def Init(path, box_pixel):
	global path_coords, box_size_pixel
	path_coords = path
	box_size_pixel = box_pixel

class Enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.max_health = 100
		self.current_health = self.max_health
		self.resistance = 0.95
		self.speed = 0.25
		self.image = pygame.Surface((30,30))
		self.image.fill(pygame.Color(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
		self.rect = self.image.get_rect()
		self.offset = (0.5*(1+self.rect.width/box_size_pixel[0]),0.5*(1+self.rect.height/box_size_pixel[1]))
		self.coords = (box_size_pixel[0]*(path_coords[0][0]-self.offset[0]),box_size_pixel[1]*(path_coords[0][1]-self.offset[1]))
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		self.current_case_number = 0
		self.position_precision = 15
		self.destination_offset = 0.15
		self.has_finished = False
		self.NewDestination()
	def Move(self):
		self.coords = (self.coords[0] + self.avance[0], self.coords[1] + self.avance[1])
		self.rect.x = self.coords[0]
		self.rect.y = self.coords[1]
		if math.sqrt((self.coords[0]-self.coords_arrivee[0])**2+(self.coords[1]-self.coords_arrivee[1])**2) < self.position_precision:
			self.current_case_number += 1
			if self.current_case_number >= len(path_coords)-1:
				self.EndPath()
			else:
				self.NewDestination()
	def NewDestination(self):
		coords_depart = (self.rect.x, self.rect.y)
		self.coords_arrivee = (box_size_pixel[0]*(path_coords[self.current_case_number+1][0]-self.offset[0]+random.uniform(-self.destination_offset,self.destination_offset)) , box_size_pixel[1]*(path_coords[self.current_case_number+1][1]-self.offset[1]+random.uniform(-self.destination_offset,self.destination_offset)))
		direction_angle = math.atan2(self.coords_arrivee[1]-coords_depart[1], self.coords_arrivee[0]-coords_depart[0])
		self.avance = (math.cos(direction_angle)*self.speed, math.sin(direction_angle)*self.speed)
	def EndPath(self):
		self.has_finished = True
	def HasFinished(self):
		return self.has_finished
