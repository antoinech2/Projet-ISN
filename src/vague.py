import time
from sys import path
path.append("../res/data/")
import vague_data

import enemy

class Vague():

	def __init__(self, game):
		self.game = game
		self.current_vague = -1
		# self.is_finished = False
		# self.time_between_enemies = 0
		# self.time_after_vague = 0
		# self.enemies = []
		# self.current_enemy_pack = 0
		# self.current_enemy_number = 0
		# self.last_spawn_time = 0
		self.NewVague()

	def NewVague(self):
		self.max_vague = len(vague_data.vagues)
		if self.current_vague +1 < self.max_vague:
			self.current_vague += 1
		data = vague_data.vagues[self.current_vague]
		self.is_finished = False
		self.time_between_enemies = data["time_between_enemies"]
		self.time_after_vague = data["time_after_vague"]
		self.enemies = data["enemies"]
		self.current_enemy_pack = 0
		self.current_enemy_number = 0
		self.last_spawn_time = time.time()
		self.current_spawned = 0

		self.total_enemies = 0
		for cur_enemy in self.enemies:
			self.total_enemies += cur_enemy[1]

	def CalcVague(self):
		if self.is_finished:
			if self.last_spawn_time + self.time_after_vague <= time.time():
				self.NewVague()
		else:
			if self.last_spawn_time + self.time_between_enemies <= time.time():
				if self.current_enemy_number >= self.enemies[self.current_enemy_pack][1]:
					if self.current_enemy_pack+1 >= len(self.enemies):
						self.is_finished = True
					else:
						self.current_enemy_pack += 1
						self.current_enemy_number = 0
				if self.is_finished == False:
					self.game.all_enemies.add(enemy.Enemy(self.game, self.enemies[self.current_enemy_pack][0]))
					self.last_spawn_time = time.time()
					self.current_enemy_number += 1
					self.current_spawned += 1
