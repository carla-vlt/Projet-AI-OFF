import random

class ChainGame:
    def __init__(self):
        self.player_scores = {'Player': 100, 'Computer': 100}

    def generate_random_chain(self, length):
        return ''.join(str(random.randint(1, 4)) for _ in range(length))

    def play_game(self):
        length = int(input("Entrez la longueur de la chaîne numérique (entre 15 et 25) : "))
        if length < 15 or length > 25:
            print("Longueur invalide. La longueur doit être comprise entre 15 et 25.")
            return

        chain = self.generate_random_chain(length)
        print("Chaîne générée :", chain)

        turn = 0
        while chain:
            player = 'Player' if turn % 2 == 0 else 'Computer'
            print("\nTour de", player)

            if player == 'Player':
                index = int(input("Entrez l'index du chiffre à supprimer (entre 1 et {}): ".format(len(chain)))) - 1
                if index < 0 or index >= len(chain):
                    print("Index invalide.")
                    continue
            else:
                # Logique de l'ordinateur
                index = self.computer_choose_index(chain)

            number = int(chain[index])
            chain = chain[:index] + chain[index+1:]

            if number % 2 == 0:
                self.player_scores[player] -= 2 * number
            else:
                other_player = 'Computer' if player == 'Player' else 'Player'
                self.player_scores[other_player] += number

            print("Score actuel - Player:", self.player_scores['Player'], "Computer:", self.player_scores['Computer'])

            # Afficher la chaîne mise à jour
            print("Chaîne mise à jour :", chain)

            turn += 1

        print("\nFin du jeu.")
        if self.player_scores['Player'] < self.player_scores['Computer']:
            print("Player gagne avec", self.player_scores['Player'], "points!")
        elif self.player_scores['Player'] > self.player_scores['Computer']:
            print("Computer gagne avec", self.player_scores['Computer'], "points!")
        else:
            print("Match nul avec", self.player_scores['Player'], "points chacun.")

    def computer_choose_index(self, chain):
        # Stratégie de l'ordinateur : choisir un index aléatoire
        return random.randint(0, len(chain) - 1)

game = ChainGame()
game.play_game()
