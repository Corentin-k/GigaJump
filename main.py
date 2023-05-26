"""
Jeu GIGA Jump réalisé en 2023 en L1 à EFREI
Projet Transverse groupe F
PAR:
    Bakiko Vénus
    Tokpinar Ismail
    Rafalimanana--Chan Peng Julien
    Assouad Adrien
    Kervagoret Corentin
    Bride Arthur
"""


import pygame
import time
from ecran import*
from jump import*
from score import*

clock = pygame.time.Clock()
pygame.time.Clock().tick(60)
# Charger les images des menus


logo_image = pygame.image.load("LOGO_JEU.png")
logo_image = pygame.transform.scale(logo_image, (window_size[0]//2, window_size[1]//3))

logo_rect = logo_image.get_rect()
logo_rect.centerx = window_size[0] // 2
logo_rect.centery = window_size[0] // 2 -75




# Définir la position et la taille du bouton
Size_button=(window_size[0]/1.5, window_size[1]/7)
button_image = pygame.image.load("Bouton_PLAY.png").convert_alpha()
button_image = pygame.transform.scale(button_image,Size_button )
button_rect = button_image.get_rect()
button_rect.center = (window_size[0] / 2, window_size[1] / 2 )

rules_button_image = pygame.image.load("Bouton_REGLES.png").convert_alpha()
rules_button_image = pygame.transform.scale(rules_button_image,Size_button)
rules_button_rect = rules_button_image.get_rect() # Créer le rectangle à partir de l'image
rules_button_rect.center = (window_size[0] / 2,window_size[1]- window_size[1] / 3)

modes_button_image = pygame.image.load("Bouton_Template_DUO.png").convert_alpha()
modes_button_image = pygame.transform.scale(modes_button_image, Size_button)
modes_button_rect = modes_button_image.get_rect()
modes_button_rect.center = (window_size[0] / 2,window_size[1]- window_size[1] / 6)

back_button_image = pygame.image.load("Bouton_carre_rtour_1.png").convert_alpha()
back_button_image = pygame.transform.scale(back_button_image, (35, 35))
back_button_rect = back_button_image.get_rect()
back_button_rect.topright = (window_size[0] - 5, 5)
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





# Variables pour le changement d'écran
menu_screen = True
game_screen = False
rules_screen = False
mode_duo=False
#Position de départ
taille_carac=character_image.get_height()
x_initial=window_size[0] // 2
y_initial= window_size[1]-(taille_carac+1/2*taille_carac)
x = x_initial
y = y_initial

LIFE=3

pygame.mixer.music.load("doodle_jump_V2_1.mp3")
pygame.mixer.music.play(-1) #Musique en Boucle

first_jump=False
speed=2
platforms = []
test=True
en_saut=False
first_iteration=True
game_image1 = pygame.image.load("Background.png")
game_image1 = pygame.transform.scale(game_image1, (window_size[0], game_image1.get_height()))
game_image2 = pygame.image.load("Background.png")
game_image2 = pygame.transform.scale(game_image2, (window_size[0], game_image2.get_height()))
game_image_y1 = -game_image1.get_height()
game_image_y2 = 0
game_images=[game_image1,game_image2,game_image_y1,game_image_y2]

print("Regle su jeu :"
              "Sauter de platfefrome en platformes pour gagner le plus de point attention vous avez trois vie "
              "a chaque fois que vous tomber en dehors de l'ecran vous perdez une vie"
              "Technique: en allant à gauche de l'écran vous vous téléporter à droite (vice-versa)"
              ""
              "Touche pour jouer :"
              "Q --> pour faire un saut à gauche"
              "Z --> pour faire un saut en hauteur"
              "D --> pour faire un saut à droite"
              )
platform_image = pygame.image.load("plateforme.png").convert_alpha()
platform_image = pygame.transform.scale(platform_image, (200, 100))

def game(LIFE):
    global y,x,platforms,first_jump,game_image_y1,game_image_y2
    j = 0

    if first_jump == False:
        platforms = init_platforms(platforms,window_size,character_image)

    elif first_jump == True:
        y += speed
        game_images[2] += speed
        game_images[3] += speed
        if game_images[2] >= window_size[1]:
            game_images[2] = -game_image1.get_height()
        if game_images[3] >= window_size[1]:
            game_images[3] = -game_image1.get_height()

        platforms, nb_platform = update_platforms(platforms, window_size, players, speed)
        if nb_platform != 0:
            platforms = generate_platform(platforms, window_size )

        pygame.display.update()
    if position_character() > window_size[1]:
        x = x_initial
        y = y_initial
        first_jump=False
        platforms= init_platforms(platforms,window_size,character_image)
        return LIFE-1
    return LIFE





# Boucle principale du jeu
while True:
    clock.tick(60)
    if position_character() < window_size[1]//4:
        speed = 5
    elif position_character() < window_size[1]//3:
        speed = 4
    elif position_character()<window_size[1]//2:
        speed=3
    else:
        speed=2
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
                        # Arrêter la musique en 1 seconde
                        pygame.mixer.music.fadeout(1000)
                    elif button.rect == rules_button_rect:
                        menu_screen = False
                        print("Afficher les règles")
                        rules_screen = True
                    elif button.rect == modes_button_rect:
                        menu_screen = False
                        mode_duo = True
                        print("Mode duo")
        elif game_screen==True or mode_duo==True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    time_pressed = pygame.time.get_ticks()
                    sens = 1
                    verif_angle=1
                elif event.key == pygame.K_d:
                    time_pressed = pygame.time.get_ticks()
                    verif_angle=1
                    sens = -1
                elif event.key == pygame.K_z:
                    time_pressed = pygame.time.get_ticks()
                    sens = -1
                    verif_angle = 0
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_q or event.key == pygame.K_d or event.key == pygame.K_z :
                    first_jump = True  # on commence a deplacer les plateformes
                    if time_pressed != 0 and LIFE!=0:

                        time_unpressed=pygame.time.get_ticks()
                        dtime=time_unpressed-time_pressed

                        x, y= jump( (x, y), dtime, sens, verif_angle, platforms, chr_sprite,game_images,LIFE,en_saut)

                        time_pressed = 0

    # Afficher l'écran du menu ou du jeu
    if menu_screen:

        window.fill((0, 0, 0))
        window.blit(game_image1, (0, 0))
        window.blit(logo_image, logo_rect)

        # Réafficher les boutons du menu principal
        buttons.add(button_sprite)
        buttons.add(rules_button_sprite)
        buttons.add(modes_button_sprite)
        buttons.draw(window)  # affiche tous les boutons

    elif game_screen:

        if LIFE==0:
            window.blit(game_image2, (0, game_images[3]))
            window.blit(game_image1, (0, game_images[2]))
            if first_iteration==True:
                score.sauvegarde_score(window,window_size,game_image1)
                first_iteration=False

            window.blit(back_button_image, back_button_rect)
            score.print_end(window,window_size)

        else:

            LIFE = game(LIFE)
            screen_play((x, y), platforms, game_images, LIFE,en_saut)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            # Retourner au menu principal
            game_screen = False
            rules_screen = False
            menu_screen = True
            pygame.mixer.music.play(-1)
            x = x_initial
            y = y_initial
            first_jump = False
            platforms = []
            LIFE=3
            score.reset()
            first_iteration = True


    elif rules_screen:
        window.blit(game_image2, (0,0))
        font = pygame.font.Font("joystix.otf", 10)
        text_lines = ["Regle du jeu :",

                      "sauter de plateforme en plateforme",
                      "pour gagner le plus de points.",

                      "Attention:",
                      "vous avez trois vies !!!",
                      "À chaque fois que vous tombez",
                      " en dehors de l'écran, ",
                      "vous perdez une vie.",

                      "Technique :",
                      "en allant à gauche de l'écran,",
                      "vous vous téléportez à droite",
                      "(et vice-versa)",

                      "Touches pour jouer :",
                      "Q --> pour faire un saut à gauche",
                      "Z --> pour faire un saut en hauteur",
                      "D --> pour faire un saut à droite"]

        y_pos = window_size[1] // 2 - len(text_lines) * 20

        for line in text_lines:
            score_text = font.render(line, True, score.text_color)
            score_rect = score_text.get_rect(center=(window_size[0] // 2, y_pos))
            window.blit(score_text, score_rect)
            y_pos += 40

        window.blit(back_button_image, back_button_rect)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            rules_screen = False
            menu_screen = True

    elif mode_duo:
        if test==True:

            window = pygame.display.set_mode(window_size_duo)
            test = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and back_button_rect.collidepoint(event.pos):
            # Retourner au menu principal
            game_screen = False
            rules_screen = False
            menu_screen = True
            pygame.mixer.music.play(-1)
            x = x_initial
            y = y_initial
            first_jump = False
            platforms = []
            LIFE = 3
            score.reset()
            first_iteration = True
        if LIFE == 0:
            if first_iteration == True:
                score.sauvegarde_score(window, window_size)
                first_iteration = False
            window.blit(game_image2, (0, game_images[3]))
            window.blit(game_image1, (0, game_images[2]))
            window.blit(back_button_image, back_button_rect)
            score.print_end(window, window_size)

        else:

            LIFE = game(LIFE)
            screen_play((x, y), platforms, game_images, LIFE,en_saut)
    pygame.display.update()

