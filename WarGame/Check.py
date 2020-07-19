from Pythonbasics.WarGame.Stats import config


class Check():
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two

    def win(self):
        if len(self.player_one.all_cards) == 0:
            print(f"\n{self.player_one.name} " + config["game"]["outOfGame"])
            print(f"{self.player_two.name} " + config["game"]["won"] + "\n")
            return True

        if len(self.player_two.all_cards) == 0:
            print(f"\n{self.player_two.name} " + config["game"]["outOfGame"])
            print(f"{self.player_one.name} " + config["game"]["won"] + "\n")
            return True

    def round_win(self, player_one_cards, player_two_cards):
        if player_one_cards[-1].value > player_two_cards[-1].value:
            self.player_one.add_cards(player_one_cards)
            self.player_one.add_cards(player_two_cards)
            self.player_one.player_won += 1
            return False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            self.player_two.add_cards(player_one_cards)
            self.player_two.add_cards(player_two_cards)
            self.player_two.player_won += 1
            return False

        else:
            return self.war_condition(player_one_cards, player_two_cards)

    def war_condition(self, player_one_cards, player_two_cards):
        print('WAR!')
        self.player_one.war_count += 1
        self.player_two.war_count += 1

        if len(self.player_one.all_cards) < 5:
            print(f"\n{self.player_one.name}" + config["war"]["gameOver"])
            print(f"{self.player_two.name}" + config["war"]["won"] + f"{self.player_one.name}" + config["war"]["lose"])
            return True
        elif len(self.player_two.all_cards) < 5:
            print(f"\n{self.player_two.name}" + config["war"]["gameOver"])
            print(f"{self.player_one.name}" + config["war"]["won"] + f"{self.player_two.name}" + config["war"]["lose"])
            return True

        else:
            for num in range(5):
                player_one_cards.append(self.player_one.remove_one())
                player_two_cards.append(self.player_two.remove_one())
            self.round_win(player_one_cards, player_two_cards)
