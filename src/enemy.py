
import pygame

class enemy(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.max_health = 100
		self.current_health = self.max_health
		self.resistance = 0.95
		self.speed = 0.8
		self.image = pygame.Surface((50,50))
		self.image.fill(pygame.Color("blue"))
		self.rect = self.image.get_rect()
		self.rect.x = 100
		self.rect.y = 100
