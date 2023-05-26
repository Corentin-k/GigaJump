import pygame

class Score:
    def __init__(self):
        self.score = 0

        self.font = pygame.font.Font("joystix.otf", 30)
        self.text_color = (0, 0, 0)
        self.name=''

    def update(self):
        self.score += 1

    def reset(self):
        self.score = 0

    def print_score(self,window):
        score_text = self.font.render("Score: {}".format(self.score), True, self.text_color)
        window.blit(score_text, (10, 10))

    def print_end(self,window,window_size):

        score_text = self.font.render("Score final:", True, self.text_color)
        score_rect = score_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 - 150))
        window.blit(score_text, score_rect)

        score_value_text = self.font.render(str(self.score), True, self.text_color)
        score_value_rect = score_value_text.get_rect(center=(window_size[0] // 2, window_size[1] // 2 -100))
        window.blit(score_value_text, score_value_rect)
        self.print_tab(window,window_size)

    def sauvegarde_score(self,window,window_size,game_image1):
        try:
            f = open("Score.txt", "a")
        except FileNotFoundError:
            f = open("Score.txt", "w")
        #creation de la zone de saisie du nom d'utilisateur
        input_box = pygame.Rect( 0,0,300, 50)
        input_box.center=(window_size[0]/2, window_size[1]/2)

        font_large = pygame.font.Font("joystix.otf", 32)

        text_lose = font_large.render("Vous avez perdu", True, self.text_color)
        text_lose_rect=text_lose.get_rect()
        text_lose_rect.center=(window_size[0] / 2, window_size[1] / 2 - 100)
        text = ''
        text_surface = self.font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = input_box.center

        ignorer_enregistrement = True
        enregistrer=False
        button_ignore = pygame.image.load("Bouton_UGN.png").convert_alpha()
        button_ignore = pygame.transform.scale(button_ignore, (300, 100))
        button_ignore_rect = button_ignore.get_rect()
        button_ignore_rect.center = (window_size[0]//2, window_size[1]/2+200)

        button_enregistre = pygame.image.load("Bouton_Valid.png").convert_alpha()
        button_enregistre = pygame.transform.scale(button_enregistre, (300, 100))
        button_enregistre_rect = button_enregistre.get_rect()
        button_enregistre_rect.center = (window_size[0] // 2 , window_size[1] / 2 + 100)

        while ignorer_enregistrement:
            # Gestion des événements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_ignore_rect.collidepoint(
                      event.pos) :
                    ignorer_enregistrement=False
                    self.name=''
                elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and button_enregistre_rect.collidepoint(
                      event.pos)) and len(text)!=0:
                    self.name = text
                    text = ''
                    enregistrer = True
                    ignorer_enregistrement = False
                elif event.type == pygame.KEYDOWN:
                    if (event.key == pygame.K_RETURN ) and len(text)!=0:
                        self.name = text
                        text = ''
                        enregistrer=True
                        ignorer_enregistrement=False

                    elif event.key == pygame.K_BACKSPACE:
                        # Efface le dernier caractère
                        text = text[:-1]
                    elif event.key != pygame.K_RETURN:
                        text += event.unicode #ajoute le caractere tapé
                    # Redessine le texte dans la zone de saisie
                    text_surface = self.font.render(text, True, (0,0,0))
                    text_rect = text_surface.get_rect()
                    text_rect.center = input_box.center
            # Dessine la zone de saisie
            window.blit(game_image1, (0, 0))
            window.blit(button_ignore, button_ignore_rect)
            window.blit(button_enregistre, button_enregistre_rect)
            pygame.draw.rect(window, (0,0,0), input_box, 5)
            window.blit(text_lose,text_lose_rect)
            window.blit(text_surface, text_rect)
            pygame.display.flip()

        if enregistrer:
            self.enregister_score()
            self.sort_tableau_score(window,window_size)

    def enregister_score(self):
        f = open("Score.txt", "a")
        print(self.name)
        f.write("{},{}\n".format(self.score, self.name))
        f.close()


    def sort_tableau_score(self,window,window_size):
        with open("Score.txt", "r") as f:
            scores = []
            for line in f:
                score, name = line.strip().split(",")
                scores.append((int(score), name))
            scores.sort(reverse=True, key=lambda x: x[0])#trie par rapport au premier element tdu tupple
        with open("Score.txt", "w") as f:
            for score,name in scores:
                f.write("{},{}\n".format(score, name))
    def print_tab(self,window,window_size):

        with open("Score.txt", "r") as f:
            tab = []
            i=1
            for line in f:
                score, name = line.strip().split(",")
                if i<4:
                    tab.append((int(score), name,i))
                elif self.name==name :
                    tab.append((int(score), name,i))
                    break
                i+=1

        for j in range(len(tab)):
            if j>2:
                score_text2 = self.font.render(" - - - ", True,
                                              self.text_color)
                score_rect2 = score_text2.get_rect(center=(window_size[0] / 2, window_size[1] / 2 + 50 * j))
                window.blit(score_text2, score_rect2)
                score_text = self.font.render("{}- {} {}".format(tab[j][2], tab[j][1], tab[j][0]), True,
                                              (0,255,0))
                score_rect = score_text.get_rect(center=(window_size[0] / 2, window_size[1] / 2 + 50 * j+50))
                window.blit(score_text, score_rect)

            else :
                if tab[j][1]==self.name:
                    color=(255,255,100)
                else:
                    color=self.text_color
                score_text = self.font.render("{}- {} {}".format(tab[j][2],tab[j][1],tab[j][0]), True, color)
                score_rect = score_text.get_rect(center=(window_size[0]/2,window_size[1]/2+50*j))
                window.blit(score_text, score_rect)



