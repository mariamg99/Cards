from game import Game
from player import Player
import time
import random

playersno = int(input("Number of players: "))
#   cardsno = int(input("Number of cards: "))
#   cper_player = int(input("Cards per player: "))
cper_player = 3     # By default in Septica

StartGame = Game(playersno, 52, 5)
random.shuffle(StartGame.cards)
print("Game Started...")

# Creating players
players = []
for i in range(playersno):

    # Distribute cards in order after shuffle
    current_cards = StartGame.current_cards[0:cper_player]
    players.append(Player(i+1, current_cards, cper_player, cper_player))

    # Update not yet distributed cards
    StartGame.current_cards = StartGame.current_cards[cper_player:StartGame.c]

winner = 0
while winner == 0:
    for p in players:
        print("\nPlayer " + str(p.id) + " started...")
        print("Cards: " + str(p.c))

        # Info about players
        print("Current player knows:")
        for a in players:
            if a.id != p.id:
                print("Player " + str(a.id) + " has " + str(len(a.c)) + " cards")
        time.sleep(0.5)

        # Actual play
        if len(StartGame.dropped_cards) > 0:
            played_card = input("Chose card to play or press N to get one ")

            if played_card == 'N' or played_card == 'n':
                p.c.extend(StartGame.current_cards[0:1])
                StartGame.current_cards = StartGame.current_cards[1:StartGame.c]
                continue
        else:
            played_card = input("Chose card to play: ")

        ok = 0
        while ok == 0:
            if played_card in p.c:
                ok = StartGame.validate_card(StartGame.dropped_cards, played_card)

                if ok == 0:
                    played_card = input("Invalid card. Press N to get a new one ")

                else:
                    p.c.remove(played_card)
                    StartGame.dropped_cards.append(played_card)
            else:
                if played_card == 'N' or played_card == 'n':
                    p.c.extend(StartGame.current_cards[0:1])
                    StartGame.current_cards = StartGame.current_cards[1:StartGame.c]
                    print(len(StartGame.current_cards))
                    ok = 2
                else:
                    print('Invalid card')
                    played_card = input("Chose card to play ")

            # game finished when a player has 0 cards
        if len(p.c) == 0:
            winner = p.id
            break
        time.sleep(1)

if winner > 0:
    print("\nPlayer " + str(winner) + " has won!")
