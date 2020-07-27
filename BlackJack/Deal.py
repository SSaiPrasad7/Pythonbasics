class Deal:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_all(self):
        return self.all_cards.clear()

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
