zahlen = [1, 2, 3, 4, 5, 6]
gerade_ungerade = ["gerade" if z % 2 == 0 else "ungerade" for z in zahlen]
print(gerade_ungerade)

noten = [1, 2, 5, 3, 5, 4, 1]
ergebnis = {"bestanden" if n <= 4 else "nicht bestanden" for n in noten}
print(ergebnis)

temperaturen = {"Wien": 23, "Graz": 31, "Linz": 12}
wetter = {stadt: "heiß" if t > 30 else "angenehm" if t > 15 else "kalt"
          for stadt, t in temperaturen.items()}
print(wetter)

print(2 + 3 * 4)
print((2 + 3) * 4)
print(2 ** 3 ** 2)
print(-2 ** 2)
print(10 - 4 - 3)
print(1 < 3 < 5)
print(not 1 == 2)
print(True or False and False)
