from Pythonbasics.TicTacToe.Screen import config


class UserDetails:
    def wantToPlay(self):
        '''
         To check whether the user wants to play the game or not
        '''
        print(config["messages"]["wantToPlay"])
        while True:
            choice = input(config["userChoice"]["yesOrNo"])
            try:
                if choice not in [config["gameControls"]["acceptPlay"], config["gameControls"]["rejectPlay"]]:
                    raise ValueError
            except ValueError:
                print(config["userChoice"]["notFound"])
                continue
            else:
                break
        return choice

    def playerDetails(self):
        '''
        To get the information about the players and players icons respectively
        '''
        print(config["welcome"]["start"])
        original_icons = config["players"]["icons"]
        icons=[]
        icons.extend(original_icons)
        players_list = {}
        player1 = input(config["players"]["player1"])
        player2 = input(config["players"]["player2"])
        icons = self.playerIcons(player1, players_list, icons)
        self.playerIcons(player2, players_list, icons)
        print(config["players"]["list"], players_list)
        icons.clear()
        return players_list

    def playerIcons(self, player, players_list, icons):
        '''
        To validate the icons selected by user
        '''
        print(icons)
        while True:
            try:
                player_icon = input(f"{player.capitalize()}" + config["userIcon"]["select"])
                if player_icon not in icons:
                    raise ValueError
            except:
                print(config["userIcon"]["notFound"])
                continue
            else:
                players_list[player] = player_icon
                icons.pop(icons.index(player_icon))
                return icons
