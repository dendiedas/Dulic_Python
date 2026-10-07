import random


def ziehung():
    zahlen = list(range(1, 46))
    for i in range(6):
        letzte = len(zahlen) - 1 - i
        index = random.randint(0, letzte)
        zahlen[index], zahlen[letzte] = zahlen[letzte], zahlen[index]
    return zahlen[-6:]


def statistik(gezogen, zaehler):
    for zahl in gezogen:
        zaehler[zahl] += 1


print("Ziehung:", ziehung())

for anzahl in [1000, 10000, 100000]:
    zaehler = {zahl: 0 for zahl in range(1, 46)}
    for i in range(anzahl):
        statistik(ziehung(), zaehler)
    print()
    print("Statistik für", anzahl, "Ziehungen:")
    for zahl, wie_oft in zaehler.items():
        print(zahl, ":", wie_oft)
