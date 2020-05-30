############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
#
# Description: Ce fichier contient le programme de gestion des
# différentes vagues d'ennemis. Il fait appraitre les ennemis
# a un moment précis en fonction de la configuration.
############################################

############################################
#Importation des modules externes:
import time
from sys import path
############################################

path.append("../res/data/")

############################################
#Importation des modules internes:
import vague_data
import enemy
############################################

class Vague():
	"Définition de la classe qui gère les vagues"
	def __init__(self, game):
		"Définition du constructeur"
		self.game = game
		self.current_vague = -1
		self.NewVague()

	def NewVague(self):
		"Méthode pour initialiser une nouvelle vague"
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
		"Méthode pour calculer la vague en cours et faire apparâitre un ennemi si besoin"
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
