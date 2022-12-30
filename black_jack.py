import playing_cards as pc

card_value = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10}

def evaluate_hand(player):
    player.hand_value = 0
    for card in player.hand:
        if card.face_value == 'ace':
            if player.hand_value + 11 > 21:
                player.hand_value += 1
            else:
                player.hand_value += 11
        else:
            player.hand_value += card_value[card.face_value]
    return player.hand_value

def play(dealer, Player1, player_hold, dealer_hold):
    deck = pc.Deck()
    deck.shuffle()

    dealer.draw(deck)
    dealer.draw(deck)
    Player1.draw(deck)
    Player1.draw(deck)

    if evaluate_hand(Player1) < player_hold:
        Player1.draw(deck)
    if evaluate_hand(dealer) < dealer_hold:
        dealer.draw(deck)
    if evaluate_hand(Player1) > 21:
        return dealer
    if evaluate_hand(dealer) > 21:
        return Player1
    if evaluate_hand(dealer) > evaluate_hand(Player1):
        return dealer
    elif evaluate_hand(Player1) > evaluate_hand(dealer):
        return Player1
    else:
        return None

trialpercent = []
dealer = pc.Player()
alice = pc.Player()
play_hold = 4
deal_hold = 4
for trial in range(play_hold, 22):
    dealer.wins = 0
    alice.wins = 0
    for n in range(0, 10001):
        winner = play(dealer, alice, play_hold,17)
        if winner is not None:
            winner.wins +=1
        dealer.foldHand()
        alice.foldHand()
    trialpercent.append(dealer.wins/(alice.wins+dealer.wins))
    trial += 1
    play_hold += 1

c=0
trial_sum = 0
highest_percent = 0
highest_value = 0

for play_hold_val in range(len(trialpercent)):
    print(f'The dealer won {trialpercent[play_hold_val]:.2%} when the player held at {play_hold_val+4}')
    if(trialpercent[play_hold_val] > highest_percent):
        highest_percent = trialpercent[play_hold_val]
        highest_value = play_hold_val + 4
    trial_sum += trialpercent[play_hold_val]
averagepercent = trial_sum / len(trialpercent)
print(f'The average percentage was {averagepercent:.2%}')
print(f'The highest percentage was {highest_percent:.2%} when player held at {highest_value}')
print(f'The difference in win percentages was {max(trialpercent) - min(trialpercent):.2%}')