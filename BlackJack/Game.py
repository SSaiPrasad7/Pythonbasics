from BlackJack.Deck import Deck
from BlackJack.Deal import Deal
from BlackJack.Account import Account
from BlackJack.Chip import Chip
from BlackJack.Gambler import Gambler


class Game:
    def __init__(self):
        self.dealer = Deal("Computer")
        self.player = Deal(input("Enter the player name: "))
        self.player_account = Account(self.player.name)
        self.player_chips = Chip(self.player.name)
        self.new_deck = Deck()
        self.gamble = Gambler(self.player, self.dealer, self.new_deck, self.player_account, self.player_chips)

    def game_intialize(self):
        self.player_chips.userChips()
        print(self.player_chips)
        self.new_deck.shuffle()
        if self.player_account.amount < self.player_chips.bet_value:
            print("\nSorry!You can't play the Game.")
            print("Out of Money!!!")
            return False
        else:
            self.game_start()
            response = self.ask_yes_no()
            if response == "Y":
                game.game_intialize()
            else:
                print("\nThank you for Playing.")

    def game_start(self):
        self.player_account.withdraw(self.player_chips.bet_value)
        self.dealer.remove_all()
        self.player.remove_all()
        for i in range(2):
            self.dealer.add_cards(self.new_deck.deal_one())
            self.player.add_cards(self.new_deck.deal_one())
        print(f"\n{self.dealer.name} Card :{self.dealer.all_cards[0]}\n")
        self.gamble.playerDisplay()
        if self.gamble.BlackJack() == False:
            self.gamble.playerOptions()
        print(self.player_account)

    def ask_yes_no(self):
        response = ""
        while response not in ["Y", "N"]:
            response = input(f"\nEnter Y to play again or N to quit game: ")
            try:
                if response not in ["Y", "N"]:
                    raise ValueError
                else:
                    return response
            except:
                print("Invalid response.Try again")


if __name__ == "__main__":
    game = Game()
    game.player_account.ask()
    game.game_intialize()
