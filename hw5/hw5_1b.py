# Blackjack
import random

def calculate_value(cards):
    value = 0
    aces = 0
    for card in cards:
        if card[0] == "ACE":
            aces += 1
            value += 11
        elif card[0] in ["JACK", "QUEEN", "KING"]:
            value += 10
        else:
            value += int(card[0])
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def display_cards(player_cards):
    results = "with the hand:"
    for card in player_cards:
        results += f" {card[0]}-{card[1]}"
    print(results)
    print()

play_again = True

while play_again:
    deck = ["ACE", "2", "3", "4", "5", "6", "7", "8", "9", "10", "JACK", "QUEEN", "KING"]
    suits = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]

    cards = [(card, suit) for suit in suits for card in deck]
    random.shuffle(cards)

    # dictionary
    hands = {
        "player": [],
        "dealer": []
    }
    
    # deal 2 cards to the player and 2 cards to the dealer
    for _ in range(2):
        hands["player"].append(cards.pop(0))
        hands["dealer"].append(cards.pop(0))

    player_busted = False
    dealer_busted = False

    while True:
        player_value = calculate_value(hands["player"])
        print(f"\nYour current value is: {player_value}")
        display_cards(hands["player"])
        if player_value > 21:
            print(f"\nYour current value is Bust! (>21)")
            player_busted = True
            break
        choice = input(f"Hit or stay? (Hit = 1, Stay = 0): ")
        if choice == "1":
            card = cards.pop(0)
            # dictionary
            print(f"You draw {card[0]}-{card[1]}")
            hands["player"].append(card)
        elif choice == "0":
            break

    while not player_busted:
        dealer_value = calculate_value(hands["dealer"])
        print(f"\nDealer's current value is: {dealer_value}")
        display_cards(hands["dealer"])
        if dealer_value < 17:
            card = cards.pop(0)
            # dictionary
            print(f"Dealer draws {card[0]}-{card[1]}")
            hands["dealer"].append(card)
            dealer_value = calculate_value(hands["dealer"])
            if dealer_value > 21:
                print(f"Dealer's current value is Bust! (>21)")
                dealer_busted = True
                break
        else:
            break

    if player_busted:
        print("*** Dealer wins! ***")
    elif dealer_busted:
        print("*** You beat the dealer! ***")
    elif player_value == dealer_value:
        print("*** You tied the dealer, nobody wins. ***")
    elif player_value > dealer_value:
        print("*** You beat the dealer! ***")
    elif player_value < dealer_value:
        print("*** Dealer wins! ***")

    play_again = input("Want to play again? (y/n): ")
    if play_again == "n":
        break

#會計系 H14126173 賈閔之
