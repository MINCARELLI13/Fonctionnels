import pygame
from pygame.locals import *

# http://sdz.tdct.org/sdz/interface-graphique-pygame-pour-python.html

# Un événement peut prendre plusieurs formes, il peut être amené par la pression ou le relâchement d'une touche du clavier,
# ou encore d'un bouton de la souris, un mouvement de la souris, du joystick, etc...
# Mais il peut aussi être un déplacement ou un redimensionnement de la fênetre !
# Un événement est donc tout ce que le programme peut "capter", de la part de l'utilisateur :
#       QUIT (croix), ACTIVEEVENT, KEYDOWN (touche enfoncée), KEYUP (touche relachée), MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, JOYAXISMOTION,
#       JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN, VIDEORESIZE, VIDEOEXPOSE, USEREVENT


# initialisation de la bibliothèque Pygame
pygame.init()

# création d'une fenêtre vide : hauteur = 640 et largeur = 480
fenetre = pygame.display.set_mode((640, 480))

# charge l'image à afficher dans la "fenetre"
fond = pygame.image.load("background.jpg").convert()

# collage du fond "background.jpg"
fenetre.blit(fond, (0,0))

# chargement et collage du personnage
personnage = pygame.image.load("perso.png").convert_alpha()
fenetre.blit(personnage, (400, 300))

# rafraîchissement de l'écran
pygame.display.flip()

continuer = 1
while continuer:
	for event in pygame.event.get():                                                    # On parcours la liste de tous les événements reçus
		if (event.type == KEYDOWN and event.key == K_LEFT) or (event.type == QUIT):     # si un de ces événements est QUIT ou Flèche gauche
			continuer = 0                                                               #On arrête la boucle
