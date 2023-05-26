import pygame
import random


PLATFORM_SPEED = 1
min_horizontal_spacing = 400
min_vertical_spacing = 100
indice=0

def add_indice():
    global indice
    indice+=1
    return indice

def generate_platform(platforms,window_size):

    PLAYER_WIDTH = window_size[0] / 5
    PLAYER_HEGHT = window_size[1] / 6
    nb_platform_max=5
    alea = random.randint(1, nb_platform_max)  # diminuer  nb_platform_max en fonction du score
    y = -250
    indice=add_indice()
    for i in range(alea):
        x = random.randint(0, int(window_size[0]))
        essai=0
        if i>1:
            while essai<30:
                x = random.randint(0, int(window_size[0]))
                overlapping = False
                for i in range(alea-1):

                    if (x>platforms[-i][0].x and abs(x - (platforms[-i][0].x+100) )<= 110) or (x<platforms[-i][0].x and (platforms[-i][0].x-(x+100))<= 110) or x>window_size[0] :
                        overlapping = True

                essai += 1
                if not(overlapping):
                    break
        if essai<10:

            platforms.append((pygame.Rect(x, y, 100, 15), indice))

        else:
            break

    return platforms

def init_platforms(platforms,window_size,character_image):
    platforms=[]
    taille_carac=character_image.get_height()
    position_platform = [
        (0, window_size[1]-taille_carac), (200,  window_size[1]-taille_carac), (400,  window_size[1]-taille_carac),
        (0, window_size[1]-3*taille_carac), (200, window_size[1]-3*taille_carac), (400, window_size[1]-3*taille_carac),
        (100, window_size[1]-5*taille_carac), (400, window_size[1]-5*taille_carac),(400, window_size[1]-5*taille_carac),
        (40, window_size[1]-7*taille_carac), (230, window_size[1]-7*taille_carac), (500, window_size[1]-7*taille_carac),
        (10,  window_size[1]-9*taille_carac), (110,  window_size[1]-9*taille_carac), (200, window_size[1]-9*taille_carac),

        ]

    #position_dict = {}
    for i in range(len(position_platform)):
            platform_rect = pygame.Rect(position_platform[i][0], position_platform[i][1], 100, 15)
            if i%3==0:
                indice=add_indice()
            platforms.append((platform_rect,indice))

    return platforms

def update_platforms(platforms,window_size,players,speed):

    for platform,indice in platforms:
        platform.y+=speed
    #for key, value in position_dict.items():
     #   value["y"]=value["y"]+speed

    # Enlever les plates-formes qui dépassent le BAS de l'écran

    platforms_to_remove = []
    position_to_remove = {}

    for platform,indice in platforms:
        if platform.top >= window_size[1]:
            platforms_to_remove.append((platform,indice))

    for platform in platforms_to_remove:
        platforms.remove(platform)

    return platforms,len(platforms_to_remove)


def draw_platforms(screen, platforms,platform_image):
    for platform,indice in platforms:
        screen.blit(platform_image, platform)





