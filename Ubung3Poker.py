import random

farben = ["Herz", "Karo", "Pik", "Kreuz"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]

deck = []
for farbe in farben:
    for wert in werte:
        deck.append([farbe, wert])


def ziehe_karten():
    return random.sample(deck, 5)


def ist_paar(hand):
    werte_in_hand = []
    for karte in hand:
        werte_in_hand.append(karte[1])
    for wert in werte_in_hand:
        if werte_in_hand.count(wert) == 2:
            return True
    return False


hand = ziehe_karten()
print(hand)
print("Paar:", ist_paar(hand))
