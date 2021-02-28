import pygame
from pygame.locals import *

# http://sdz.tdct.org/sdz/interface-graphique-pygame-pour-python.html

# initialisation de la bibliothèque pygame
pygame.init()

# création d'une fenêtre d'affichage : largeur = 600 pixels, hauteur = 480 pixels
fenetre = pygame.display.set_mode((640,480), RESIZABLE)                 # "RESIZABLE" signifie qu'on peut redimensionner la "fenetre"

# chargement de l'image "background.jpg" dans la variable "fond"
fond = pygame.image.load("background.jpg").convert()                    # ".convert()" convertit l'image dans un format compatible avec pygame

# collage du "fond" dans la "fenetre" au point de coordonnées (0,0 )
fenetre.blit(fond, (0,0))

# chargement et collage du personnage
personnage = pygame.image.load("perso.png").convert_alpha() # "_alpha()" rend transparent le petit carré dans lequel se trouve le personnage
fenetre.blit(personnage, (0, 0))

# calcul du rapport d'échelle entre le personnage et le fond afin de le garder constant dans la suite
scale = (100 + 100) / (640 + 480)

# affichage du contenu de la "fenetre"
pygame.display.flip()

continuer = 1
 
while continuer:
 
    for event in pygame.event.get():
 
        if event.type == QUIT:
            continuer = 0
 
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                continuer = 0
        
        if event.type == VIDEORESIZE:           # VIDEORESIZE  : size(nouvelle_largeur, nouvelle_hauteur), w = nouvelle_largeur, h = nouvelle_hauteur
            fenetre = pygame.display.set_mode((event.w, event.h), RESIZABLE)    # modification de la taille de la fenêtre
            fond = pygame.image.load("background.jpg").convert()        # non indispensable mais mieux pour avoir une bonne qualité d'image
            fond = pygame.transform.scale(fond, (event.w, event.h))             # modification de la taille de l'image de fond
            personnage = pygame.image.load("perso.png").convert_alpha() # non indispensable mais mieux pour avoir une bonne qualité d'image
            personnage = pygame.transform.scale(personnage, (round(event.w * scale), round(event.h * scale)))   # modification de la taille du personnage
 
    fenetre.blit(fond, (0,0))
    fenetre.blit(personnage, (0, 0))
    pygame.display.flip()
 
pygame.quit()



# # création d'une fenêtre d'affichage : largeur = 600 pixels, hauteur = 480 pixels
# fenetre = pygame.display.set_mode((600, 480), RESIZABLE)    # "RESIZABLE" signifie qu'on peut redimensionner la "fenetre"

# # chargement de l'image "background.jpg" dans la variable "fond"
# fond = pygame.image.load("background.jpg")

# # collage du "fond" dans la "fenetre" au point de coordonnées (0,0 )
# fenetre.blit(fond, (0,0))

# # affichage du contenu de la "fenetre"
# pygame.display.flip()

# # chargement et collage du personnage
# personnage = pygame.image.load("perso.png").convert_alpha()
# fenetre.blit(personnage, (10, 10))

# # rafraîchissement de l'écran
# pygame.display.flip()

# # VIDEORESIZE  : size(nouvelle_largeur, nouvelle_hauteur), w = nouvelle_largeur, h = nouvelle_hauteur

# # attend la fermeture de la "fenetre" grâce à la croix
# continuer = 1
# while continuer:
# 	for event in pygame.event.get():                                                    # On parcours la liste de tous les événements reçus

# 		if (event.type == KEYDOWN and event.key == K_LEFT) or (event.type == QUIT):     # si un de ces événements est QUIT ou Flèche gauche
# 			continuer = 0

# 		if event.type == VIDEORESIZE:
# 			# fenetre = pygame.display.set_mode((event.w, event.h), RESIZABLE)
# 			fond = pygame.transform.scale(fond, (event.w, event.h))
# 			print(event.size, event.w, event.h)
# 			#pygame.display.flip()

#     fenetre.blit(fond, (0,0))
#     pygame.display.flip()
# pygame.quit()
