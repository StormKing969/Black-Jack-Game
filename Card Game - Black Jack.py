import random 

Player_Cards = []
Dealer_Cards = []

def Value(cards):
    current = sum(cards)
    return current

while len(Dealer_Cards) != 2:
    Dealer_Cards.append(random.randint(1, 11))
    if len(Dealer_Cards) == 2:
        print("Dealer has X &", Dealer_Cards[1])
        dealer_total = Value(Dealer_Cards)


while len(Player_Cards) != 2:
    Player_Cards.append(random.randint(1, 11))
    if len(Player_Cards) == 2:
        print("Player has", Player_Cards)
        player_total = Value(Player_Cards)

if dealer_total == 21:
    print("Dealer wins with a total of 21")
elif dealer_total > 21:
    print("Dealer has busted")

while Value(Player_Cards) < 21:
    choice = str(input("Stay or Hit? ")).lower()
    if choice == "hit":
        Player_Cards.append(random.randint(1, 11))
        print("Player has", Player_Cards)
    else:
        print("Dealer has a total of " + str(Value(Dealer_Cards)) + " with", Dealer_Cards) 
        print("Player has a total of " + str(Value(Player_Cards)) + " with", Player_Cards) 
        if Value(Dealer_Cards) > Value(Player_Cards):
            print("Dealer wins")
            break
        else:
            print("Player wins")
            break

if Value(Player_Cards) > 21:
    print("Player has busted")
elif Value(Player_Cards) == 21:
    print("Player win with a Blackjack")

print("Goodbye")