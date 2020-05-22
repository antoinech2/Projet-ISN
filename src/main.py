############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 0.4.0-InDev
# Programme Python 3.7
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 0.4.0-InDev
#
# Description: Ce fichier contient le programme principal qui gère
# la création de la fenêtre et la gestion de la boucle principale
# Il appelle les fonctions pour afficher les éléments à l'écran,
# ou analyser les évènements utilisateurs.
############################################

############################################
#Importation des modules externes:
import pygame
import time
############################################

############################################
#Importation des modules internes:
import map_generator
import map_drawing
import enemy
import tower
import time
import interfaces
############################################

############################################
#Définition de la Class principale pour les constantes de jeu
class Game():
	"Class principale"
	############################################
	#Définition des constantes générales du jeu:
	SCREEN_FORMAT = 9/16
	DEFAULT_SCREEN_SIZE = (992,558)
	MIN_SCREEN_SIZE = (750,422)
	MAP_SIZE = (16,9)

	TICK_TIME = 0.008 #Temps d'attente entre deux ticks (en secondes)
	############################################

	def __init__(self):
		#Initialisation du jeu
		self.current_gui = "game"
		self.is_game_running = True
		self.current_tick = 0
		self.last_second = time.time()
		self.current_fps = 0
		self.last_fps = 0

		self.health = 2000
		self.money = 100
		self.ennemies_killed = 0

		#Initialisation des ennemis
		self.all_enemies = pygame.sprite.Group()
		#Initialisation des tours
		self.all_towers = pygame.sprite.Group()
		self.all_projectiles = pygame.sprite.Group()
		self.placing_tower = pygame.sprite.GroupSingle()

		self.screen_size = Game.DEFAULT_SCREEN_SIZE
		self.global_ratio = 1
		#Initialisation de la fenêtre
		self.screen = pygame.display.set_mode(Game.DEFAULT_SCREEN_SIZE, pygame.RESIZABLE)
		pygame.display.set_caption("Tower Defense v0.3")

		#Génération du chemin aléatoire
		self.path_coords = map_generator.CalculateNewPath(Game.MAP_SIZE)
		#Génération graphique du rendu de la carte
		self.map_surface, self.box_size_pixel, self.map_rect_list = map_drawing.CreateMapSurface(Game.MAP_SIZE,self.path_coords, self.screen_size)

	def Run(self):
		#Boucle principale
		while self.is_game_running:
			self.current_tick += 1
			self.current_fps += 1
			if self.last_second +1 <= time.time():
				self.last_second = time.time()
				self.last_fps = self.current_fps
				self.current_fps = 0
			time.sleep(Game.TICK_TIME)

			#Lecture des événements
			for event in pygame.event.get():
				#Quitter le jeu
				if event.type == pygame.QUIT:
					self.is_game_running = False
				#Redimention de la fenêtre
				elif event.type == pygame.VIDEORESIZE:
					diff = (abs(event.w-self.screen_size[0]),abs(event.h-self.screen_size[1]))
					if diff[0] > diff[1]:
						w = max(Game.MIN_SCREEN_SIZE[0],event.w)
						new_width, new_height = w, int(w*Game.SCREEN_FORMAT)
					else:
						h = max(Game.MIN_SCREEN_SIZE[1],event.h)
						new_width, new_height = int(h/Game.SCREEN_FORMAT), h

					changed_ratio = new_width/self.screen_size[0]
					self.global_ratio = new_width/Game.DEFAULT_SCREEN_SIZE[0]
					pygame.display.set_mode((new_width,new_height), pygame.RESIZABLE)
					self.screen_size = (new_width, new_height)
					self.map_surface, self.box_size_pixel = map_drawing.ResizeMapSurface(Game.MAP_SIZE, self.screen_size, self.map_surface)
					for current_enemy in self.all_enemies:
						current_enemy.UpdatePosition(changed_ratio)
						current_enemy.NewDestination()

				#Evenements lors de la partie
				if self.current_gui == "game":
					#Ajout d'une tour avec la touche T
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_t:
							self.placing_tower.add(tower.Tower(self, 0))
					#Placement de la tour avec le clic de la souris
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if self.placing_tower.sprite != None:
							new_tower = self.placing_tower.sprite.PlaceTower(event.pos)
							if new_tower:
								self.all_towers.add(new_tower)
								self.placing_tower.empty()

			#Boucle lors de la partie
			if self.current_gui == "game":

				#Calcul du tick
				#Ajout d'un ennemi tous les 100 ticks
				if self.current_tick%100 == 0:
					self.all_enemies.add(enemy.Enemy(self, 0))
				#Avancement des ennemis et suppression des ennemis qui sont au bout du chemin
				for current_enemy in self.all_enemies:
					#current_enemy.TakeDamage(random.random())
					current_enemy.Move()
				#Changement de la couleur de la tour en placement en fonction des collisions
				for current_tower in self.placing_tower:
					current_tower.CursorPlace(pygame.mouse.get_pos())
				#Attaque des tours déjà placées
				for current_tower in self.all_towers:
					current_tower.Shot()
				for current_projectile in self.all_projectiles:
					current_projectile.Move()

				#Affichage à l'écran
				self.screen.blit(self.map_surface,(0,0))
				self.placing_tower.draw(self.screen)
				if self.placing_tower.sprite != None:
					self.placing_tower.sprite.DisplayRange()
					self.placing_tower.sprite.Display()
				for current_tower in self.all_towers:
					current_tower.DisplayLifeBar()
				self.all_towers.draw(self.screen)
				self.all_enemies.draw(self.screen)
				self.all_projectiles.draw(self.screen)
				self.screen.blit(interfaces.RenderBottomGUI(self),(0,self.screen_size[1]*0.8))
				self.screen.blit(interfaces.RenderRightGUI(self.screen_size, self.health, self.money, len(self.all_towers), len(self.all_enemies), self.ennemies_killed, self.last_fps),(self.screen_size[0]*0.8,0))
				for current_enemy in self.all_enemies:
					current_enemy.DisplayLifeBar()
					if current_enemy.rect.collidepoint(pygame.mouse.get_pos()):
						self.screen.blit(interfaces.ShowEnnemyStats(self, current_enemy), (0,self.screen_size[1]*0.8))
				for current_tower in self.all_towers:
					if current_tower.rect.collidepoint(pygame.mouse.get_pos()):
						current_tower.DisplayRange()
						self.screen.blit(interfaces.ShowTowerStats(self, current_tower), (0,self.screen_size[1]*0.8))
			#Boucle lors de l'écran de fin
			elif self.current_gui == "game_lost":
				self.screen.fill(pygame.Color("blue"))
				interfaces.RenderText("Fin de partie.", 80, "red", (self.screen_size[0]/2, self.screen_size[1]/4), self.screen)
				interfaces.RenderText("Vous n'avez plus de vies.", 50, "yellow", (self.screen_size[0]/2, self.screen_size[1]/4+100), self.screen)

			#Rafraîchissement de l'écran
			pygame.display.flip()

		#Arrêt de pygame lorsque on sort de la boucle
		pygame.quit()
	############################################

#Définition de la fonction principale:
def __main__():
	"Fonction principale"

	pygame.init() #Démarrage de pygame

	#Initialisation du jeu
	game = Game()
	game.Run()

__main__()
