import pygame
import time
from math import *

from ecran import*
from platforms import*

last_platform_index=-1
def detect_collision( position, descente, platforms, chr_sprite,game_images):
    global last_platform_index
    x, y = position

    # Vérification si le joueur est en dehors de l'écran
    if y > window_size[1] + 200:
        return True, x, y
    if   y<0:#empeche d'aller trop haut d'en l'ecran
        return False,x,y
    # Vérification de collision avec les plateformes
    platform_sprites = []
    for platform,indice in platforms:
        sprite = pygame.sprite.Sprite()
        sprite.rect = platform
        platform_sprites.append((sprite, indice))

    collision_list = []
    collision_sprites = pygame.sprite.spritecollide(chr_sprite, [sprite for sprite, _ in platform_sprites], False)
    for sprite in collision_sprites:
        for platform_sprite, indice in platform_sprites:
            if sprite == platform_sprite:
                collision_list.append((sprite, indice))
                break
    if len(collision_list) > 0:
        platform_rect = collision_list[0][0].rect
        platform_index =collision_list[0][1]
        if chr_sprite.rect.bottom <= platform_rect.top + 5 and chr_sprite.rect.colliderect(
                platform_rect) and descente == True:
            # Vérification si le joueur est sur le bord gauche ou droit de la plateforme
            if platform_index > last_platform_index:
                score.update()
                last_platform_index = platform_index

            y = platform_rect.top - chr_sprite.rect.height / 2

            return True, x, y

    return False, x, y

def jump(position,dtime, sens, verif_angle,platforms,chr_sprite,game_images,LIFE,en_saut):
    speed = 4  # vitesse augmente avec dtime
    gravity = 0.27
    if dtime >=900:
        dtime = 900
    if verif_angle==1:
        gravity= gravity - (dtime /6000)
        angle = 1.2 - (dtime / 20000)
    else:
        gravity=gravity-(dtime/5000) #mettre une limite
        angle=1.571
    x,y=position
    o_y = y
    o_x = x
    position_precedente=1000
    temps = 1
    descente = False

    while True:
        x = o_x - sens * temps * cos(angle) * speed
        y = ((gravity * ((x - o_x) ** 2)) / (2 * (10 ** 2) * (cos(angle) ** 2))) + sens * (x - o_x) * tan(angle) + o_y

        if x < 0:
            x = window_size[0] + x
        elif x > window_size[0]:
            x = x-window_size[0]
        if position_precedente < y:
            descente = True
        position_precedente = y
        Booleen_collision,x, y =detect_collision((x,y),descente,platforms,chr_sprite,game_images)
        if not(Booleen_collision) :
            screen_play((x,y),platforms,game_images,LIFE,True)
            pygame.time.wait(1)
        else:
            screen_play((x, y), platforms, game_images, LIFE,True)
            break
        temps+=1
    return x,y

