import pygame, sys
from button import Button
import random
import tkinter as tk
from tkinter import messagebox
from random import randint, choice


pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def play():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.fill("black")
        PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
        PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(PLAY_TEXT, PLAY_RECT)

        PLAY_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    ask()

        pygame.display.update()



def generate_random_string(length):
    """
    Génère une chaîne aléatoire de chiffres entre 1 et 4 avec une longueur donnée.

    Args:
    length (int): Longueur de la chaîne à générer.

    Returns:
    str: Chaîne aléatoire de chiffres entre 1 et 4.
    """
    return ''.join(str(random.randint(1, 4)) for _ in range(length))

def display_game_window(random_strings):
    joueur1 = 100
    joueur2 = 100
    random_strings = [generate_random_string(15)]
    pygame.init()

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 640

    # Création de la fenêtre
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("20th Group AI Game")

    font = pygame.font.Font(None, 32)
    input_font = pygame.font.Font(None, 24)

    input_rect = pygame.Rect(10, SCREEN_HEIGHT - 40, 100, 30)  # Définition du champ de saisie
    input_text = ""  # Variable pour stocker le texte saisi par l'utilisateur

    current_player = 1

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Récupérer la saisie de l'utilisateur
                    if input_text.isdigit():
                        index = int(input_text) - 1  # Convertir l'entrée en indice de chaîne (0-indexé)
                        if 0 <= index < len(random_strings[-1]):
                            removed_number = int(random_strings[-1][index])
                            new_string = random_strings[-1][:index] + random_strings[-1][index+1:]

                            # Ajouter la chaîne actuelle à l'historique
                            random_strings.append(new_string)

                            # Mettre à jour le score du joueur
                            if removed_number % 2 == 0:
                                joueur1 -= removed_number * 2
                            else:
                                joueur2 += removed_number

                            # Passer au joueur suivant
                            current_player = 2 if current_player == 1 else 1

                            # Effacer le champ de saisie après chaque saisie réussie
                            input_text = ""

            # Gérer la saisie de l'utilisateur
            elif event.type == pygame.TEXTINPUT:
                if event.text.isdigit() and len(input_text) < 2:  # Limiter la longueur de la saisie à 2 caractères
                    input_text += event.text
                elif event.text == "\x08":  # Gérer la touche de suppression (backspace)
                    input_text = input_text[:-1]

        screen.fill(WHITE)
        
        # Affichage de la chaîne aléatoire
        text_surface = font.render(random_strings[-1], True, BLACK)
        text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text_surface, text_rect)

        # Affichage des scores des joueurs et du tour du joueur
        joueur_surface = font.render("Joueur 1: " + str(joueur1), True, BLACK)
        joueur_rect = joueur_surface.get_rect(topleft=(10, 10))
        screen.blit(joueur_surface, joueur_rect)

        joueur2_surface = font.render("Joueur 2: " + str(joueur2), True, BLACK)
        joueur2_rect = joueur2_surface.get_rect(topleft=(10, 40))
        screen.blit(joueur2_surface, joueur2_rect)

        chaine = font.render("Chaine avant suppression ",True, BLACK)
        chaine_rect = chaine.get_rect(topleft=(500, 10))
        screen.blit(chaine, chaine_rect)

        turn_surface = font.render("Tour du Joueur " + str(current_player), True, BLACK)
        turn_rect = turn_surface.get_rect(topleft=(10, 70))
        screen.blit(turn_surface, turn_rect)

        # Affichage de l'historique des chaînes avant suppression
        for i, s in enumerate(random_strings[:-1]):
            previous_string_surface = font.render(f"", True, BLACK)
            previous_string_rect = previous_string_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10 + 30 * i))
            screen.blit(previous_string_surface, previous_string_rect)

            previous_string_value_surface = font.render(s, True, BLACK)
            previous_string_value_rect = previous_string_value_surface.get_rect(topright=(SCREEN_WIDTH - 10, 40 + 30 * i))
            screen.blit(previous_string_value_surface, previous_string_value_rect)

        # Affichage du champ de saisie
        pygame.draw.rect(screen, BLACK, input_rect, 2)
        input_surface = input_font.render(input_text, True, BLACK)
        screen.blit(input_surface, (input_rect.x + 5, input_rect.y + 5))

        pygame.display.flip()



def test2():
        print("Fonction test2() appelée")


def ask():
    # Couleurs
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    # Création de la fenêtre
    screen = pygame.display.set_mode((800, 640))
    pygame.display.set_caption("Bouton et barre de recherche")

    # Chargement des images
    joueur_image = pygame.image.load("assets/PLAYER.png")
    joueur_image = pygame.transform.scale(joueur_image, (200, 200))
    joueur_rect = joueur_image.get_rect(center=(250, 300))

    computer_image = pygame.image.load("assets/COMPUTER.png")
    computer_image = pygame.transform.scale(computer_image, (200, 200))
    computer_rect = computer_image.get_rect(center=(550, 300))

    remplace_image = pygame.image.load("assets/PLAYER2.png")
    remplace_image = pygame.transform.scale(remplace_image, (200, 200))

    remplace_image2 = pygame.image.load("assets/COMPUTER2.png")
    remplace_image2 = pygame.transform.scale(remplace_image2, (200, 200))

    # Police et variables de texte
    font = pygame.font.Font(None, 32)
    search_text = ""
    search_rect = pygame.Rect(100, 500, 600, 35)
    search_active = False
    enter_rect = pygame.Rect(350, 590, 100, 35)
    text_under_search = ""

    # Fonction pour afficher quelque chose
    def afficher1():
        print("Fonction afficher1() appelée")

    def afficher2():
        print("Fonction afficher2() appelée")

    def entrer():
        print("Fonction entrer() appelée")

    # Fonction pour générer une chaîne de longueur 'number'

    # Gérer les événements
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if joueur_rect.collidepoint(event.pos):
                    afficher1()
                elif computer_rect.collidepoint(event.pos):
                    afficher2()
                elif search_rect.collidepoint(event.pos):
                    search_active = True
                else:
                    search_active = False
                if joueur_rect and enter_rect.collidepoint(event.pos) :
                    if search_text.isdigit():
                        number = int(search_text)
                        if 15 <= number <= 25:
                            entrer()
                            random_string = generate_random_string(number)
                            print("Chaîne aléatoire générée :", random_string)
                            random_string = generate_random_string(number)
                            display_game_window(random_string)
                        else:
                            text_under_search = "Saisir un chiffre entre 15 et 25"
                            search_text = ""
                    else:
                        text_under_search = "Saisir un chiffre entre 15 et 25"
                        search_text = ""
                if computer_rect.collidepoint(event.pos):
                    test2()
                    app = NumStringGameApp()
                    app.mainloop()



            elif event.type == pygame.KEYDOWN:
                if search_active:
                    if event.key == pygame.K_RETURN:
                        if 15 <= len(search_text) <= 25 and search_text.isdigit():
                            entrer()
                            random_string = generate_random_string(int(search_text))
                            print("Chaîne aléatoire générée :", random_string)
                          

                            
                        elif not (15 <= len(search_text) <= 25):
                            text_under_search = "Saisir un chiffre entre 15 et 25"
                            search_text = ""
                    elif event.key == pygame.K_BACKSPACE:
                        search_text = search_text[:-1]
                    else:
                        search_text += event.unicode

        screen.fill(WHITE)

        # Dessiner les éléments
        pygame.draw.rect(screen, BLACK, joueur_rect, 2)
        if joueur_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(remplace_image, joueur_rect)
        else:
            screen.blit(joueur_image, joueur_rect)

        pygame.draw.rect(screen, BLACK, computer_rect, 2)
        if computer_rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(remplace_image2, computer_rect)
        else:
            screen.blit(computer_image, computer_rect)

        pygame.draw.rect(screen, BLACK, search_rect, 2)
        search_surface = font.render(search_text, True, BLACK)
        screen.blit(search_surface, (search_rect.x + 5, search_rect.y + 5))
        pygame.draw.rect(screen, BLACK, search_rect, 2)

        if text_under_search:
            text_surface = font.render(text_under_search, True, BLACK)
            screen.blit(text_surface, (search_rect.x, search_rect.bottom + 5))

        pygame.draw.rect(screen, BLACK, enter_rect, 2)
        enter_surface = font.render("Entrer", True, BLACK)
        screen.blit(enter_surface, (enter_rect.x + 5, enter_rect.y + 5))

        pygame.display.flip()



def afficher_ecran_blanc():
    SCREEN.fill("white")

    # Couleur blanche
    BLANC = (255, 255, 255)

    # Création de la fenêtre

    pygame.display.set_caption("Écran blanc")

    # Boucle principale
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Remplissage de l'écran avec la couleur blanche
        SCREEN.fill(BLANC)

        # Rafraîchissement de l'écran
        pygame.display.flip()

        # Couleurs
   

    # Fonction pour afficher les messages des joueurs
def afficher_messages(joueur1, joueur2):
        BLANC = (255, 255, 255)
        NOIR = (0, 0, 0)

        # Dimensions de la fenêtre
        largeur, hauteur = 400, 200

        # Police de texte
        police = pygame.font.SysFont(None, 24)

        # Textes
        texte_joueur1 = ""
        texte_joueur2 = ""
       
        fenetre = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Messages des joueurs")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            fenetre.fill(BLANC)

            # Affichage des messages des joueurs
            texte1 = police.render(joueur1, True, NOIR)
            fenetre.blit(texte1, (50, hauteur//2))

            texte2 = police.render(joueur2, True, NOIR)
            fenetre.blit(texte2, (largeur - 50 - texte2.get_width(), hauteur//2))

            pygame.display.flip()

    # Fonction principale
def afficher():
       
        BLANC = (255, 255, 255)
        NOIR = (0, 0, 0)

        # Dimensions de la fenêtre
        largeur, hauteur = 400, 200

        # Police de texte
        police = pygame.font.SysFont(None, 24)
    
        # Textes
        texte_joueur1 = ""
        texte_joueur2 = ""
       
        # Création de la fenêtre principale
        fenetre_principale = pygame.display.set_mode((largeur, hauteur))
        pygame.display.set_caption("Barres de recherche")
        fenetre_principale.fill(BLANC)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Gestion de la saisie dans la barre de recherche pour joueur 1
                elif event.type == pygame.KEYDOWN and len(texte_joueur1) < 10:
                    if event.key == pygame.K_BACKSPACE:
                        texte_joueur1 = texte_joueur1[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(texte_joueur1) > 0 and len(texte_joueur2) > 0:
                            afficher_messages(texte_joueur1, texte_joueur2)
                    else:
                        texte_joueur1 += event.unicode

                # Gestion de la saisie dans la barre de recherche pour joueur 2
                elif event.type == pygame.KEYDOWN and len(texte_joueur2) < 10:
                    if event.key == pygame.K_BACKSPACE:
                        texte_joueur2 = texte_joueur2[:-1]
                    elif event.key == pygame.K_RETURN:
                        if len(texte_joueur1) > 0 and len(texte_joueur2) > 0:
                            afficher_messages(texte_joueur1, texte_joueur2)
                    else:
                        texte_joueur2 += event.unicode

            # Affichage de la barre de recherche pour joueur 1
            pygame.draw.rect(fenetre_principale, NOIR, (50, 50, 200, 30), 2)
            texte_barre1 = police.render(texte_joueur1, True, NOIR)
            fenetre_principale.blit(texte_barre1, (55, 55))
            
            # Affichage de la barre de recherche pour joueur 2
            pygame.draw.rect(fenetre_principale, NOIR, (50, 100, 200, 30), 2)
            texte_barre2 = police.render(texte_joueur2, True, NOIR)
            fenetre_principale.blit(texte_barre2, (55, 105))

            # Bouton Entrer
            if len(texte_joueur1) > 0 and len(texte_joueur2) > 0:
                pygame.draw.rect(fenetre_principale, NOIR, (160, 150, 80, 30), 2)
                texte_bouton = police.render("Entrer", True, NOIR)
                fenetre_principale.blit(texte_bouton, (180, 155))
           
            pygame.display.flip()
    

def options():
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("white")

        OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_BACK = Button(image=None, pos=(640, 460), 
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        pygame.display.update()

class NumStringGameApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("20th Group AI Game")
        self.geometry("800x600")
        self.resizable(False, False)

        self.player_score = 100
        self.computer_score = 100
        self.current_turn = choice(["Player", "Computer"])
        self.num_string = ""

        self.create_widgets()

    def create_widgets(self):
        length_frame = tk.Frame(self)
        length_frame.pack(pady=20)

        self.length_label = tk.Label(length_frame, text="String Length (15-25):")
        self.length_label.pack(side=tk.LEFT)

        self.length_entry = tk.Entry(length_frame, width=5)
        self.length_entry.pack(side=tk.LEFT)

        self.start_button = tk.Button(length_frame, text="Start Game", command=self.start_game)
        self.start_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(length_frame, text="Reset Game", command=self.reset_game, state='disabled')
        self.reset_button.pack(side=tk.LEFT)

        self.game_area_frame = tk.Frame(self)
        self.game_area_frame.pack(pady=10, expand=True)

        self.move_entry = tk.Entry(self.game_area_frame, width=5, state=tk.DISABLED)
        self.move_entry.pack(side=tk.LEFT)

        self.move_button = tk.Button(self.game_area_frame, text="Make Move", command=self.make_move, state=tk.DISABLED)
        self.move_button.pack(side=tk.LEFT)

        self.score_label = tk.Label(self, text="Player Score: 100 | Computer Score: 100")
        self.score_label.pack(pady=(5, 0))
        self.turn_label = tk.Label(self, text="")
        self.turn_label.pack(pady=(5, 10))

    def start_game(self):
        try:
            length = int(self.length_entry.get())
            assert 15 <= length <= 25
        except (ValueError, AssertionError):
            messagebox.showerror("Error", "Invalid length. Please enter a number between 15 and 25.")
            return

        self.num_string = ''.join(str(randint(1, 4)) for _ in range(length))
        self.update_game_area()
        self.reset_button.config(state='normal')

    def update_game_area(self, clear=False):
        if clear:
            self.num_string_label.config(text="")
            self.score_label.config(text="Player Score: 100 | Computer Score: 100")
            self.turn_label.config(text="")
            return

        if hasattr(self, 'num_string_label'):
            self.num_string_label.config(text=self.num_string)
        else:
            self.num_string_label = tk.Label(self, text=self.num_string)
            self.num_string_label.pack(pady=(10, 0))

        self.score_label.config(text=f"Player Score: {self.player_score} | Computer Score: {self.computer_score}")
        self.turn_label.config(text=f"{self.current_turn}'s Turn")

        if self.current_turn == "Player":
            self.move_entry.config(state=tk.NORMAL)
            self.move_button.config(state=tk.NORMAL)
        else:
            self.move_entry.config(state=tk.DISABLED)
            self.move_button.config(state=tk.DISABLED)

    def make_move(self):
        if self.current_turn != "Player":
            messagebox.showinfo("Wait", "It's not your turn yet!")
            return

        move_position = self.move_entry.get()
        if not move_position.isdigit() or int(move_position) < 1 or int(move_position) > len(self.num_string):
            messagebox.showerror("Invalid Move", "Please enter a valid position.")
            return

        move_position = int(move_position) - 1
        removed_number = int(self.num_string[move_position])
        self.num_string = self.num_string[:move_position] + self.num_string[move_position + 1:]

        if removed_number % 2 == 0:
            self.player_score -= removed_number * 2
        else:
            self.computer_score += removed_number

        self.update_game_area()
        self.move_entry.delete(0, tk.END)

        if not self.num_string:
            self.end_game()
            return

        self.current_turn = "Computer"
        self.after(500, self.computer_move)

    def computer_move(self):
        if not self.num_string:
            self.end_game()
            return

        # Select strategy based on a condition or user input. For now, it's random selection for illustration.
        strategy = choice(['first', 'random'])
        if strategy == 'first':
            best_move = 0  # Always picks the first number
        elif strategy == 'random':
            best_move = randint(0, len(self.num_string) - 1)  # Picks a random number

        # Apply the move
        removed_number = int(self.num_string[best_move])
        self.num_string = self.num_string[:best_move] + self.num_string[best_move + 1:]

        if removed_number % 2 == 0:
            self.computer_score -= removed_number * 2
        else:
            self.player_score += removed_number

        self.update_game_area()

        if not self.num_string:
            self.end_game()
            return

        self.current_turn = "Player"
        self.move_entry.config(state=tk.NORMAL)  # Re-enable the move entry for the player
        self.move_button.config(state=tk.NORMAL)

    def end_game(self):
        # Determine the winner based on the scores
        if self.player_score < self.computer_score:
            result_text = "Player wins!"
        elif self.computer_score < self.player_score:
            result_text = "Computer wins!"
        else:
            result_text = "It's a draw!"

        # Show the game over message
        messagebox.showinfo("Game Over",
                            f"{result_text}\nFinal Scores:\nPlayer: {self.player_score}\nComputer: {self.computer_score}")

        # Enable the reset button after the game ends
        self.reset_button.config(state='normal')

    def reset_game(self):
        # Reset the game to its initial state
        self.player_score = 100
        self.computer_score = 100
        self.current_turn = choice(["Player", "Computer"])
        self.num_string = ""

        # Clear UI elements
        self.length_entry.config(state=tk.NORMAL)
        self.length_entry.delete(0, tk.END)
        self.start_button.config(state=tk.NORMAL)
        self.move_entry.delete(0, tk.END)
        self.move_entry.config(state=tk.DISABLED)
        self.move_button.config(state=tk.DISABLED)
        self.reset_button.config(state='disabled')  # Disable the reset button until the game starts again

        # Clear the game area
        if hasattr(self, 'num_string_label'):
            self.num_string_label.config(text="")
        self.score_label.config(text="Player Score: 100 | Computer Score: 100")
        self.turn_label.config(text="")




def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    ask()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
                

        pygame.display.update()

main_menu()
