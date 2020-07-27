class Chip:
    def __init__(self,name):
        self.name=name
        self.chips = {1: 0, 10: 0, 100: 0, 500: 0}
        self.bet_value = 0

    def __str__(self):
        return f"\n{self.name} bet is ${self.bet_value}."

    def userChips(self):
        self.bet_value = 0
        print(f"----------------------")
        print(f"| ${1} | ${10} | ${100} | ${500} |")
        print(f"----------------------")
        print("Place your Bets \n")
        self.chipInput()
        chips_list = list(self.chips.keys())
        value_list = list(self.chips.values())
        for i in range(len(chips_list)):
            self.bet_value += value_list[i] * chips_list[i]

    def chipInput(self):
        try:
            for x in self.chips.keys():
                self.chips[x] = int(input(f"Enter the number of {x}'s chip: "))
        except:
            print("Invalid chip number.Try Again ")
            self.chipInput()
