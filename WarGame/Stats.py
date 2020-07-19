from tabulate import tabulate
from Pythonbasics.WarGame.Helper import Helper
config=Helper().readConfig("English.json")
class Stats:
    def __init__(self,player_one,player_two):
        self.player_one=player_one
        self.player_two=player_two
    def gameStats(self):
        played = self.player_one.player_won + self.player_two.player_won + self.player_one.war_count
        print(config["board"]["display"])
        print(config["board"]["line"])
        headers = ['Players', 'Player1', 'Player2']
        row1=["Name", self.player_one.name, self.player_two.name]
        row2=["No of Cards", len(self.player_one.all_cards), len(self.player_two.all_cards)]
        row3=["No of Times Won", self.player_one.player_won, self.player_two.player_won]
        row4=["No of Times at WAR",self.player_one.war_count,self.player_two.war_count]
        row5=["No of Played",played,played]
        content=[row1,row2,row3,row4,row5]
        tablefmt = 'orgtbl'
        table = tabulate(content,headers,tablefmt)
        print(table)
        print(config["board"]["line"])


