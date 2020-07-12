from WarGame.Deck import Deck
from WarGame.Player import Table

new_deck = Deck()
new_deck.shuffle()
player_one = Table()
player_two = Table()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

if len(player_one.all_cards) == 0:
    print("Player One out of cards! Game Over")
    print("Player Two Wins!")

if len(player_two.all_cards) == 0:
    print("Player Two out of cards! Game Over")
    print("Player One Wins!")

player_one_cards = []
player_one_cards.append(player_one.remove_one())

player_two_cards = []
player_two_cards.append(player_two.remove_one())

if player_one_cards[-1].value > player_two_cards[-1].value:
    print(f"{player_one.name} has won this round")
    player_one.add_cards(player_one_cards)
    player_one.add_cards(player_two_cards)

elif player_one_cards[-1].value < player_two_cards[-1].value:
    print(f"{player_two.name} has won this round")
    player_two.add_cards(player_one_cards)
    player_two.add_cards(player_two_cards)
else:
    print('WAR!')

    if len(player_one.all_cards) < 5:
        print("Player One unable to play war! Game Over at War")
        print("Player Two Wins! Player One Loses!")


    elif len(player_two.all_cards) < 5:
        print("Player Two unable to play war! Game Over at War")
        print("Player One Wins! Player One Loses!")
    else:
        for num in range(5):
            player_one_cards.append(player_one.remove_one())
            player_two_cards.append(player_two.remove_one())
