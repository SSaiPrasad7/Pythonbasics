class UserDetails:
    def wantToPlay(self):
        choice = "123"
        in_range = False
        while choice.isalpha() == False or in_range == False:
            choice = input("Enter Y for Yes or N for No ")
            if choice.isalpha() == False:
                print("Sorry, but you did not enter a Character. Try again.")
            if choice not in ["Y", "N"]:
                print("Sorry, but you did not choose Y or N option")
            else:
                in_range = True
                return choice

    def playerDetails(self):
        # Players name
        icons = ['!', '@', '#', '$', '%', '^', '&', '*', 'X', 'O']
        players_list = {}
        player1 = input("Enter the Player1 name: ")
        player2 = input("Enter the Player2 name: ")
        icons = self.playerIcons(player1, players_list, icons)
        self.playerIcons(player2, players_list, icons)
        return players_list

    def playerIcons(self, player, players_list,icons):
        print(icons)
        in_range = False
        while in_range == False:
            # selection of icon
            player_icon = input(f'{player} select one icon from the above set: ')
            if player_icon not in icons:
                print("Choose the icon from the above set only")
            else:
                players_list[player] = player_icon
                icons.pop(icons.index(player_icon))
                in_range = True
        return icons
