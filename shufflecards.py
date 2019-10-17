import random
from collections import namedtuple

Card = namedtuple('Card', ['value', 'suit'])
suits = ['hearts', 'diamonds', 'spades', 'clubs']
unused_cards = [Card(value, suit) for value in range(1, 14) for suit in suits]

used_cards = []
player_1_hand = []
player_2_hand = []
# deal five cards to player 1
for i in range(26):
    drawn_card = random.choice(unused_cards)
    used_cards.append(drawn_card)
    unused_cards = [f for f in unused_cards if f not in used_cards]
    player_1_hand.append(drawn_card)
# repeat the process for player 2
for i in range(26):
    drawn_card = random.choice(unused_cards)
    used_cards.append(drawn_card)
    player_2_hand.append(drawn_card)
    unused_cards = [f for f in unused_cards if f not in used_cards]
print(f"Player1 cards : {player_1_hand}")
print(f"Player2 cards : {player_2_hand}")