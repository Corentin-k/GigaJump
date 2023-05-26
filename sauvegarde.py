import pygame
import time
from math import *
import random
from jump import*
from ecran import*
# Initialisation de Pygame
pygame.init()
# Définir les dimensions de la fenêtre
fen = pygame.display.get_desktop_sizes()
fps = 60
clock = pygame.time.Clock()

window,window_size=init_variable(fen)
# Charger les images des menus
menu_image = pygame.image.load("fond.png")
menu_image = pygame.transform.scale(menu_image, (550, window_size[1]))
rules_image = pygame.image.load("regles.png")
rules_image = pygame.transform.scale(rules_image, (550,  window_size[1]))

# Image Jeu



# Définir la position et la taille du bouton
button_image = pygame.image.load("bouton.png").convert_alpha()
button_image = pygame.transform.scale(button_image, (200, 75))
button_rect = pygame.Rect(0, 0, 200, 100)
button_rect.center = (window_size[0] // 2,  window_size[1] // 2 )

rules_button_image = pygame.image.load("bouton-regles.png").convert_alpha()
rules_button_image = pygame.transform.scale(rules_button_image, (200, 75))
rules_button_rect = pygame.Rect(0, 0, 200, 100)
rules_button_rect.center = (window_size[0] // 2,  window_size[1] // 2 + 150)

modes_button_image = pygame.image.load("bouton-modes.png").convert_alpha()
modes_button_image = pygame.transform.scale(modes_button_image, (200, 75))
modes_button_rect = pygame.Rect(0, 0, 200, 100)
modes_button_rect.center = (window_size[0] // 2,  window_size[1] // 2 + 300)

back_button_image = pygame.image.load("bouton-retour.png").convert_alpha()
back_button_image = pygame.transform.scale(back_button_image, (50, 50))
back_button_rect = back_button_image.get_rect()
back_button_rect.topright = ( window_size[0] - 10, 10)

# Créer un groupe de sprites pour les boutons
buttons = pygame.sprite.Group()
button_sprite = pygame.sprite.Sprite()
button_sprite.image = button_image
button_sprite.rect = button_rect
buttons.add(button_sprite)

rules_button_sprite = pygame.sprite.Sprite()
rules_button_sprite.image = rules_button_image
rules_button_sprite.rect = rules_button_rect
buttons.add(rules_button_sprite)

modes_button_sprite = pygame.sprite.Sprite()
modes_button_sprite.image = modes_button_image
modes_button_sprite.rect = modes_button_rect
buttons.add(modes_button_sprite)





# Varaibles pour le changment d'écran
menu_screen = True
game_screen = False
rules_screen = False
test = True
test1 = True
# Variables por le déplacement

x_initial = 400
y_initial = 400
x = x_initial
y = y_initial
a = radians(30)
speed = 23
a = 1.3
g = 0.12
pygame.mixer.music.load("doodle_jump_V2_1.mp3")
pygame.mixer.music.play(-1)



# Boucle principale du jeu
while True:
    clock.tick(60)
    time = 0

    # Gérer les événements

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Vérifier si un bouton est cliqué
            for button in buttons:
                if button.rect.collidepoint(event.pos):
                    # Cacher tous les boutons
                    buttons.empty()
                    # Vérifier quel bouton est cliqué et modifier l'état de l'écran en conséquence
                    if button.rect == button_rect:
                        menu_screen = False
                        game_screen = True
                        # Arrêter la musique en 1 secondes
                        pygame.mixer.music.fadeout(1000)
                    elif button.rect == rules_button_rect:
                        menu_screen = False
                        print("Afficher les règles")
                        rules_screen = True
                    elif button.rect == modes_button_rect:
                        print("Afficher les modes de jeu")

    # Afficher l'écran du menu ou du jeu
    if menu_screen:

        window.fill((0, 0, 0))
        window.blit(menu_image, (0, 0))
        # Réafficher les boutons du menu principal
        buttons.add(button_sprite)
        buttons.add(rules_button_sprite)
        buttons.add(modes_button_sprite)
        buttons.draw(window)  # affiche tous les boutons

    elif game_screen:

        screen_play(window,window_size,(x, y))
        keys = pygame.key.get_pressed()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            # Retourner au menu principal
            game_screen = False
            rules_screen = False
            menu_screen = True
            pygame.mixer.music.play(-1)
            x = x_initial
            y = y_initial

        if keys[pygame.K_q]:
            time = pygame.time.get_ticks()
            a = 1.3
            sens = 1
        if keys[pygame.K_d]:
            time = pygame.time.get_ticks()
            a = 1.3
            sens = -1
        if keys[pygame.K_z]:
            time = pygame.time.get_ticks()
            sens = -1
            a = 1.571

    elif rules_screen:

        window.fill((0, 0, 0))
        window.blit(rules_image, (0, 0))
        window.blit(back_button_image, back_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            # Retourner au menu principal
            rules_screen = False
            menu_screen = True
    if time != 0:
        x,y=jump(window,window_size,time, sens, a)
    pygame.display.update()

    """
    valid_platforms = []
        valid_dict= {}
        # Parcourir chaque plate-forme dans la liste des plates-formes

        for platform in platforms:
            # Si la plate-forme est encore dans l'écran, ajouter à la liste des plates-formes valides
            if platform.bottom >= -200:
                valid_platforms.append(platform)
                for key, value in position_dict.items():
                    if value["x"] == platform.left and value["y"] == platform.top:
                        valid_dict[len(valid_dict)] = {'x': platform.left, 'y': platform.top}
        # Remplacer la liste des plates-formes avec la nouvelle liste ne contenant que les plates-formes valides
        platforms = valid_platforms
        position_dict =valid_dict
    """

    """
       for key, value in position_to_remove.items():
           del position_dict[key]
       """
    """"
        for i, pos in enumerate(position_platform):
            x, y = pos
            position_dict[i] = {'x': x, 'y': y}
        """
    """
                for key, value in position_dict.items():
                    if value["x"] == platform.left and value["y"] == platform.top:
                        position_to_remove[key] = value
                """

def update_score():
    global score
    score+=1
    return score
def init_score():
    global score
    score=0
