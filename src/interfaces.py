import pygame

def RenderRightGUI(screen_size, game_health):
	gui_size = (0.2*screen_size[0],screen_size[1])
	gui = pygame.Surface(gui_size)
	gui.fill(pygame.Color("gray"))
	RenderText("Vies:"+str(game_health), 20, "green", (gui_size[0]-50, 20), gui)
	return gui

def RenderText(texte, taille, color, coords, surface, centered = True):
	text = pygame.font.Font("../res/fonts/Righteous-Regular.ttf", taille).render(texte, True, pygame.Color(color))
	rect = text.get_rect()
	if centered:
		rect.center = coords
	surface.blit(text,rect)
