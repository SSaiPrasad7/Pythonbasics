class Gambler:
    def __init__(self, player, dealer, new_deck, player_account, player_chips):
        self.dealer_total = 0
        self.player_total = 0
        self.new_deck = new_deck
        self.player = player
        self.dealer = dealer
        self.player_chips = player_chips
        self.player_account = player_account

    def calculate(self, player, dealer):
        self.dealer_total = 0
        self.player_total = 0
        for i in range(len(dealer.all_cards)):
            if dealer.all_cards[i].value == 11:
                if self.dealer_total > 10:
                    self.dealer_total += 1
                else:
                    self.dealer_total += dealer.all_cards[i].value
            else:
                self.dealer_total += dealer.all_cards[i].value
        for j in range(len(player.all_cards)):
            if player.all_cards[j].value == 11:
                if self.player_total > 10:
                    self.player_total += 1
                else:
                    self.player_total += player.all_cards[j].value
            else:
                self.player_total += player.all_cards[j].value

    def ask_one_two(self):
        response = ""
        while response not in ["0", "1"]:
            response = input(f"Select {0} or {1} from the above options: ")
            try:
                if response not in ["0", "1"]:
                    raise ValueError
                else:
                    return response
            except:
                print("Invalid option.Try again")

    def BlackJack(self):
        if self.dealer_total == self.player_total:
            self.dealerDisplay()
            self.player_account.deposit(self.player_chips.bet_value)
            print("\nPush")
            return True
        elif self.player_total == 21:
            self.dealerDisplay()
            print("\nBlack Jack")
            self.player_account.deposit(2.5 * self.player_chips.bet_value)
            return True
        return False

    def playerOptions(self):
        print("\nGame Options ")
        print("0.Stand \n1.Hit ")
        option = self.ask_one_two()
        if option == "0":
            self.stand()
        if option == "1":
            self.hit()
        return option

    def hit(self):
        self.player.add_cards(self.new_deck.deal_one())
        self.playerDisplay()
        while True:
            choice = self.playerOptions()
            if choice == "0":
                break

    def stand(self):
        self.dealerDisplay()
        if self.player_total > 21:
            print(f"\n{self.player.name} lost the bet amount of {self.player_chips.bet_value}")
            print(f"{self.dealer.name} Won!!!")

        elif self.dealer_total < 17:
            self.dealer.add_cards(self.new_deck.deal_one())
            self.calculate(self.player, self.dealer)
            self.stand()
        else:
            self.game_conditions()

    def game_conditions(self):
        if self.dealer_total == self.player_total:
            self.player_account.deposit(self.player_chips.bet_value)
            print("\nPush")

        elif self.player_total == 21:
            self.player_account.deposit(2 * self.player_chips.bet_value)
            print(f"\n{self.player.name} won the bet amount of {self.player_chips.bet_value}")
            print(f"{self.player.name}  Won!!!")

        elif self.dealer_total == 21:
            print(f"\n{self.player.name} lost the bet amount of {self.player_chips.bet_value}")
            print(f"{self.dealer.name}  Won!!!")

        elif self.dealer_total > 21 or self.player_total > self.dealer_total:
            self.player_account.deposit(2 * self.player_chips.bet_value)
            print(f"\n{self.player.name} won the bet amount of {self.player_chips.bet_value}")
            print(f"{self.player.name}  Won!!!")

        elif self.player_total > 21 or self.dealer_total > self.player_total:
            print(f"\n{self.player.name} lost the bet amount of {self.player_chips.bet_value}")
            print(f"{self.dealer.name}  Won!!!")

    def playerDisplay(self):
        self.calculate(self.player, self.dealer)
        print(f"\n{self.player.name} is currently at {self.player_total}")
        print(f"{self.player.name}'s Cards:")
        for i in range(len(self.player.all_cards)):
            print(f"\t{self.player.all_cards[i]}")

    def dealerDisplay(self):
        self.calculate(self.player, self.dealer)
        print(f"\n{self.dealer.name} is currently at {self.dealer_total}")
        print(f"{self.dealer.name} Cards:")
        for i in range(len(self.dealer.all_cards)):
            print(f"\t{self.dealer.all_cards[i]}")
