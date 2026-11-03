import random

farben = ["Herz", "Karo", "Pik", "Kreuz"]
werte = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "D", "K", "A"]

deck = []
for farbe in farben:
    for wert in werte:
        deck.append([farbe, wert])


def ziehe_karten():
    return random.sample(deck, 5)


def hole_werte(hand):
    werte_in_hand = []
    for karte in hand:
        werte_in_hand.append(karte[1])
    return werte_in_hand


def ist_paar(hand):
    werte_in_hand = hole_werte(hand)
    for wert in werte_in_hand:
        if werte_in_hand.count(wert) == 2:
            return True
    return False


def ist_zwei_paare(hand):
    werte_in_hand = hole_werte(hand)
    anzahl = 0
    for wert in werte_in_hand:
        if werte_in_hand.count(wert) == 2:
            anzahl += 1
    return anzahl == 4


def ist_drilling(hand):
    werte_in_hand = hole_werte(hand)
    for wert in werte_in_hand:
        if werte_in_hand.count(wert) == 3:
            return True
    return False


hand = ziehe_karten()
print(hand)
print("Paar:", ist_paar(hand))
print("Zwei Paare:", ist_zwei_paare(hand))
print("Drilling:", ist_drilling(hand))
