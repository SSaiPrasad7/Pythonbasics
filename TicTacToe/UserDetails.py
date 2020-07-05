class UserDetails:
    def wantToPlay(self):
        '''
         To check whether the user wants to play the game or not
        '''
        while True:
            choice = input("Enter Y for Yes or N for No ")
            try:
                if choice not in ["Y", "N"]:
                    raise ValueError
            except ValueError:
                print("Sorry, but you did not choose Y or N option")
                continue
            else:
                break
        return choice

    def playerDetails(self):
        '''
        To get the information about the players and players icons respectively
        '''
        icons = ['!', '@', '#', '$', '%', '^', '&', '*', 'X', 'O']
        players_list = {}
        player1 = input("Enter the Player1 name: ")
        player2 = input("Enter the Player2 name: ")
        icons = self.playerIcons(player1, players_list, icons)
        self.playerIcons(player2, players_list, icons)
        return players_list

    def playerIcons(self, player, players_list, icons):
        '''
        To validate the icons selected by user
        '''
        print(icons)
        while True:
            try:
                player_icon = input(f'{player.capitalize()} select one icon from the above set: ')
                if player_icon not in icons:
                    raise ValueError
            except:
                print("Choose the icon from the above set only")
                continue
            else:
                players_list[player] = player_icon
                icons.pop(icons.index(player_icon))
                return icons
