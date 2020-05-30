############################################
# INFORMATIONS / DESCRIPTION:
# Jeu Tower Defense Version 1.2.0
# Programme Python 3.7 ou 3.8
# Auteurs: Titouan Escaille, Antoine Cheucle
# Encodage: UTF-8
# Licence: Aucune
# Version: 1.2.0
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
import interfaces
import vague
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
		"Initialisation du jeu"
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
		self.screen = pygame.display.set_mode(Game.DEFAULT_SCREEN_SIZE) #, pygame.RESIZABLE (Redimension désactivée temporairement)
		pygame.display.set_caption("Tower Defense v1.2.0")

		#Génération du chemin aléatoire
		self.path_coords = map_generator.CalculateNewPath(Game.MAP_SIZE)
		#Génération graphique du rendu de la carte
		self.map_surface, self.box_size_pixel, self.map_rect_list = map_drawing.CreateMapSurface(Game.MAP_SIZE,self.path_coords, self.screen_size)

		self.vague = vague.Vague(self)
		tower.InitTowers()

	def Run(self):
		"Boucle principale du jeu"
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
					pygame.display.set_mode((new_width,new_height)) #, pygame.RESIZABLE
					self.screen_size = (new_width, new_height)
					self.map_surface, self.box_size_pixel = map_drawing.ResizeMapSurface(Game.MAP_SIZE, self.screen_size, self.map_surface)
					for current_enemy in self.all_enemies:
						current_enemy.UpdatePosition(changed_ratio)
						current_enemy.NewDestination()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						if self.current_gui == "game":
							self.current_gui = "pause"
						else:
							self.current_gui = "game"

				#Evenements lors de la partie
				if self.current_gui == "game":
					#Placement de la tour avec le clic de la souris
					if event.type == pygame.MOUSEBUTTONDOWN:
						if self.placing_tower.sprite != None:
							new_tower = self.placing_tower.sprite.PlaceTower(event.pos)
							if new_tower:
								self.all_towers.add(new_tower)
							self.placing_tower.empty()
						else:
							tower_type_collision = interfaces.CheckMouseCollision(self)
							if tower_type_collision != None:
								self.placing_tower.add(tower.Tower(self, tower_type_collision))

			#Boucle lors de la partie
			if self.current_gui == "game":

				#CALCUL DU TICK

				#Calcul de la vague (apparition des ennemis si nécessaire)
				self.vague.CalcVague()
				#Avancement des ennemis et suppression des ennemis qui sont au bout du chemin
				for current_enemy in self.all_enemies:
					current_enemy.Move()
				#Changement de la couleur de la tour en placement en fonction des collisions
				for current_tower in self.placing_tower:
					current_tower.CursorPlace(pygame.mouse.get_pos())
				#Attaque des tours déjà placées
				for current_tower in self.all_towers:
					current_tower.Shot()
				#Avancée des projectiles vers leurs ennemis
				for current_projectile in self.all_projectiles:
					current_projectile.Move()

				#AFFICHAGE A L'ECRAN

				#Affichage de la map de fond
				self.screen.blit(self.map_surface,(0,0))
				#Affichage des tours en placement
				self.placing_tower.draw(self.screen)
				#Affichage du range et des informations de la tour en placement
				if self.placing_tower.sprite != None:
					self.placing_tower.sprite.DisplayRange()
					self.placing_tower.sprite.Display()
				#Affichage de la barre de vie de toutes les tours.
				for current_tower in self.all_towers:
					current_tower.DisplayLifeBar()
				#Affichage des tours, ennemis et projectiles
				self.all_towers.draw(self.screen)
				self.all_enemies.draw(self.screen)
				self.all_projectiles.draw(self.screen)
				#Affichage des menus graphiques latéraux
				self.screen.blit(interfaces.RenderBottomGUI(self),(0,self.screen_size[1]*0.8))
				self.screen.blit(interfaces.RenderRightGUI(self),(self.screen_size[0]*0.8,0))
				tower_type_collision = interfaces.CheckMouseCollision(self)
				if tower_type_collision != None:
					self.screen.blit(interfaces.ShowPlacementTowerStats(self, tower_type_collision),(0,self.screen_size[1]*0.8))
				#Affichage des barres de vie des ennemis et les statistiques de l'ennemi sélectionné.
				for current_enemy in self.all_enemies:
					current_enemy.DisplayLifeBar()
					if current_enemy.rect.collidepoint(pygame.mouse.get_pos()):
						self.screen.blit(interfaces.ShowEnnemyStats(self, current_enemy), (0,self.screen_size[1]*0.8))
				#Affichage du rayon et des statistiques de la tour sélectionnée
				for current_tower in self.all_towers:
					if current_tower.rect.collidepoint(pygame.mouse.get_pos()):
						current_tower.DisplayRange()
						self.screen.blit(interfaces.ShowTowerStats(self, current_tower), (0,self.screen_size[1]*0.8))
			elif self.current_gui == "pause":
				interfaces.RenderText("Jeu en pause.", 80, "red", (self.screen_size[0]/2, self.screen_size[1]/4), self.screen)
				interfaces.RenderText("Appuyez sur 'P' pour reprendre le jeu.", 45, "blue", (self.screen_size[0]/2-100, self.screen_size[1]/4+100), self.screen)


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
