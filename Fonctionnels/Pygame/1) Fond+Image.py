import pygame
import time

# Un événement peut prendre plusieurs formes, il peut être amené par la pression ou le relâchement d'une touche du clavier,
# ou encore d'un bouton de la souris, un mouvement de la souris, du joystick, etc...
# Mais il peut aussi être un déplacement ou un redimensionnement de la fênetre !
# Un événement est donc tout ce que le programme peut "capter", de la part de l'utilisateur :
#       QUIT (croix), ACTIVEEVENT, KEYDOWN (touche enfoncée), KEYUP (touche relachée), MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN, JOYAXISMOTION,
#       JOYBALLMOTION, JOYHATMOTION, JOYBUTTONUP, JOYBUTTONDOWN, VIDEORESIZE, VIDEOEXPOSE, USEREVENT


# création d'une fenêtre d'affichage : largeur = 600 pixels, hauteur = 480 pixels
fenetre = pygame.display.set_mode((640, 480))

# chargement de l'image "background.jpg" dans la variable "fond"
fond = pygame.image.load("background.jpg").convert()    # ".convert()" convertit l'image dans un format compatible avec pygame

# collage du "fond" dans la "fenetre" au point de coordonnées (0,0 )
fenetre.blit(fond, (0,0))

# affichage du contenu de la "fenetre"
pygame.display.flip()

# chargement et collage du personnage "perso.png"
personnage = pygame.image.load("perso.png").convert_alpha() # "_alpha()" rend transparent le petit carré dans lequel se trouve le personnage
fenetre.blit(personnage, (0, 0))

# rafraîchissement de l'écran
pygame.display.flip()

# mise en pause du programme pendant 3 secondes
time.sleep(3)
