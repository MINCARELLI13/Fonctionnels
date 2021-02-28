import pygame
from pygame.locals import *
import time

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

# charge l'image "background.jpg" à afficher dans la "fenetre"
fond = pygame.image.load("fond_mcg.jpg").convert()

# collage du fond "background.jpg"
fenetre.blit(fond, (0,0))

# chargement du personnage
perso = pygame.image.load("macgyver.png").convert_alpha()
# récupère les positions d'une image rectangulaire (coord_haut_gauche, coord_bas_droite)
position_perso = perso.get_rect()
# collage du personnage dans la "fenetre"
fenetre.blit(perso, position_perso)

# rafraîchissement de l'écran
pygame.display.flip()

continuer = 1

# permet d'effectuer un déplacement (haut, bas...) plusieurs fois en laissant la touche enfoncée
# 400 ms = délai avant de commencer les déplacements successifs et 30 ms = temps entre chaque déplacement
pygame.key.set_repeat(400, 30)

mouvements = {K_DOWN:(0,10), K_UP:(0,-10), K_RIGHT:(10,0), K_LEFT:(-10,0)}

while continuer:

	for event in pygame.event.get():        # on parcours la liste de tous les événements reçus

		if event.type == QUIT:              # si un de ces événements est QUIT
			continuer = 0                   # on arrête la boucle

		if event.type == KEYDOWN:
			position_perso = position_perso.move(mouvements[event.key])

		# if (event.type == KEYDOWN) and (event.key == K_DOWN):	# flèche vers le bas
		# 	position_perso = position_perso.move(0, 3)
		# if (event.type == KEYDOWN) and (event.key == K_UP):		# flèche vers le haut
		# 	position_perso = position_perso.move(0, -3)
		# if (event.type == KEYDOWN) and (event.key == K_RIGHT):	# flèche vers la droite
		# 	position_perso = position_perso.move(3, 0)
		# if (event.type == KEYDOWN) and (event.key == K_LEFT):	# flèche vers la gauche
		# 	position_perso = position_perso.move(-3, 0)
		
	fenetre.blit(fond, (0,0))		# on réaffiche le fond pour nettoyer l'ancienne position du personnage
	fenetre.blit(perso, position_perso)	# on réaffiche le personnage à sa nouvelle position
	pygame.display.flip()					# on rafraichit l'écran



