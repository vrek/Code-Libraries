"""An script to automatically run many games of blackjack"""
import pandas as pd
import playing_cards as pc

card_value = {'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9, 'ten':10, 'jack':10, 'queen':10, 'king':10}

def evaluate_hand(player):
    """Function to evaluate the value of a blackjack hand"""
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

def play(playdeal, player_1, player_hold, dealer_hold):
    """Function to play a hand of blackjack"""
    deck = pc.Deck()
    deck.shuffle()

    playdeal.draw(deck)
    playdeal.draw(deck)
    player_1.draw(deck)
    player_1.draw(deck)

    if evaluate_hand(player_1) < player_hold:
        player_1.draw(deck)
    if evaluate_hand(playdeal) < dealer_hold:
        playdeal.draw(deck)
    if evaluate_hand(player_1) > 21:
        return playdeal
    if evaluate_hand(playdeal) > 21:
        return player_1
    if evaluate_hand(playdeal) > evaluate_hand(player_1):
        return playdeal
    elif evaluate_hand(player_1) > evaluate_hand(playdeal):
        return player_1
    else:
        return None

house_win_percent = []
dealer = pc.Player()
alice = pc.Player()
play_hold = 4
deal_hold = 4
for dealertrial in range(deal_hold,22):
    house_win_percent.append([])
    play_hold = 4
    for playertrial in range(play_hold, 22):
        house_win_percent[dealertrial-4].append([])
        dealer.wins = 0
        alice.wins = 0
        for n in range(0, 101):
            winner = play(dealer, alice, play_hold, deal_hold)
            if winner is not None:
                winner.wins +=1
            dealer.foldHand()
            alice.foldHand()
        house_win_percent[dealertrial-4][playertrial-4]=(dealer.wins/alice.wins+dealer.wins)
        play_hold += 1
    deal_hold +=1
df = pd.DataFrame.from_records(house_win_percent)

#(['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'],
#     columns = ['4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21'])
print(df)

#trial_sum = 0
#highest_percent = 0
#highest_value = 0
#
#for play_hold_val in range(len(trialpercent)):
#    print(f'The player won {trialpercent[play_hold_val]:.2%} when the player held at {play_hold_val+4}')
#    if trialpercent[play_hold_val] > highest_percent:
#        highest_percent = trialpercent[play_hold_val]
#        highest_value = play_hold_val + 4
#    trial_sum += trialpercent[play_hold_val]
#averagepercent = trial_sum / len(trialpercent)
#print(f'The average percentage was {averagepercent:.2%}')
#print(f'The highest percentage was {highest_percent:.2%} when player held at {highest_value}')
#print(f'The difference in win percentages was {max(trialpercent) - min(trialpercent):.2%}')
