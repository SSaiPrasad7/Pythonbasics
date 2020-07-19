from Pythonbasics.WarGame.Deck import Deck
from Pythonbasics.WarGame.Player import Table
from Pythonbasics.WarGame.Check import Check
from Pythonbasics.WarGame.Stats import Stats, config


class Game:
    def play(self):
        choice = Game().ask_yes_no()
        if choice == config["gameControls"]["acceptPlay"]:
            (player_one, player_two) = Game().gameStart()
            check = Check(player_one, player_two)
            board = Stats(player_one, player_two)
            board.gameStats()
            game_off = False
            while game_off==False:
                (player_one_cards, player_two_cards) = Game().displayCard(player_one, player_two)
                win_at_war = check.round_win(player_one_cards, player_two_cards)
                if check.win() == True or win_at_war == True:
                    board.gameStats()
                    game_off=True
            Game().play()
        else:
            print(config["endGame"]["message"])
            return False

    def ask_yes_no(self):
        response =""
        print(config["messages"]["wantToPlay"])
        while response not in (config["gameControls"]["acceptPlay"], config["gameControls"]["rejectPlay"]):
            response = input(config["userChoice"]["yesOrNo"])
            try:
                if response not in (config["gameControls"]["acceptPlay"], config["gameControls"]["rejectPlay"]):
                    raise ValueError
                else:
                    return response
            except:
                print(config["userChoice"]["notFound"])


    def gameStart(self):
        print(config["welcome"]["start"])
        new_deck = Deck()
        new_deck.shuffle()
        player1_name = input(config["players"]["player1"])
        player_one = Table(player1_name.capitalize())
        player2_name = input(config["players"]["player2"])
        player_two = Table(player2_name.capitalize())
        for i in range(26):
            player_one.add_cards(new_deck.deal_one())
            player_two.add_cards(new_deck.deal_one())

        return player_one, player_two

    def displayCard(self, player_one, player_two):
        player_one_cards = []
        player_two_cards = []
        player_one_cards.append(player_one.remove_one())
        player_two_cards.append(player_two.remove_one())
        return player_one_cards, player_two_cards


if __name__ == "__main__":
    Game().play()