import pygame
from platforms import*
import score

from score import*
pygame.init()
def init_window():
    # Définir les dimensions de la fenêtre
    fen = pygame.display.get_desktop_sizes()
    window_width = fen[0][0]/3
    window_height = fen[0][1]-100
    window_size = (window_width, window_height)
    # Créer la fenêtre
    character_image = pygame.image.load("Moai_statue_png_tete_sigma_ombre.png")
    pygame.display.set_icon(character_image)
    window = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Doodle")
    #Possibilité de changer l'icone

    return window,window_size

coeur = pygame.image.load("coeur.png")
coeur = pygame.transform.scale(coeur, (35, 35))
coeur_vide = pygame.image.load("coeur_vide.png")
coeur_vide = pygame.transform.scale(coeur_vide, (35, 35))

def screen_play(position,platforms,game_images,LIFE,en_saut):
    global score
    if en_saut==True:
        chr_sprite.image = character_image_saut
    else:
        chr_sprite.image = character_image

    chr_sprite.rect.center = position
    window.blit(game_images[0], (0, game_images[2]))
    window.blit(game_images[1], (0, game_images[3]))
    j=0
    for i in range (LIFE):
        j+=1
        window.blit(coeur, (back_button_rect[0] -40 *j,back_button_rect[1]))
    for i in range (3-LIFE):
        j += 1
        window.blit(coeur_vide, (back_button_rect[0] -40*j,back_button_rect[1]))
    draw_platforms(window, platforms,platform_image)
    players.draw(window)
    score.print_score(window)
    window.blit(back_button_image, back_button_rect)
    pygame.display.update()

def variable_game(window,window_size):



    back_button_image = pygame.image.load("Bouton_carre_rtour_1.png").convert_alpha()
    back_button_image = pygame.transform.scale(back_button_image, (35, 35))
    back_button_rect = back_button_image.get_rect()
    back_button_rect.topright = (window_size[0] - 5, 5)

    character_image = pygame.image.load("Moai_statue_png_tete_niais_ombre.png")
    character_image_saut = pygame.image.load("Moai_statue_png_tete_sigma_ombre.png")
    character_image = pygame.transform.scale(character_image, (window_size[0]/7, window_size[1]/8))
    character_image_saut = pygame.transform.scale(character_image_saut, (window_size[0] / 7, window_size[1] / 8))
    character_width = character_image.get_size()
    chrRect = character_image.get_rect()
    players = pygame.sprite.Group()
    chr_sprite = pygame.sprite.Sprite()
    chr_sprite.image = character_image
    chr_sprite.rect = chrRect

    players.add(chr_sprite)

    return back_button_image,back_button_rect,chr_sprite,players,chrRect,character_image,character_image_saut



def position_character():
    return chrRect.y


window,window_size=init_window()
window_size_duo=(window_size[0]*2,window_size[1])
windows_size_simple=window_size



back_button_image,back_button_rect,chr_sprite,players,chrRect,character_image,character_image_saut=variable_game(window,window_size)
score=Score()



platform_image = pygame.image.load("plateforme.png").convert_alpha()
platform_image = pygame.transform.scale(platform_image, (100, 15))

