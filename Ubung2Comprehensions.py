# List Comprehension mit if/else:
# [ausdruck_wenn_wahr if bedingung else ausdruck_sonst for element in iterable]
zahlen = [1, 2, 3, 4, 5, 6]
gerade_ungerade = ["gerade" if z % 2 == 0 else "ungerade" for z in zahlen]
print(gerade_ungerade)

# Set Comprehension mit if/else (Duplikate fallen weg, Reihenfolge egal)
noten = [1, 2, 5, 3, 5, 4, 1]
ergebnis = {"bestanden" if n <= 4 else "nicht bestanden" for n in noten}
print(ergebnis)

# Dict Comprehension mit if/else: {schluessel: wert for ...}
temperaturen = {"Wien": 23, "Graz": 31, "Linz": 12}
wetter = {stadt: "heiß" if t > 30 else "angenehm" if t > 15 else "kalt"
          for stadt, t in temperaturen.items()}
print(wetter)

# Unterschied: if/else VOR dem for wandelt jedes Element um,
# ein if NACH dem for filtert Elemente heraus (kein else möglich)
nur_gerade = [z for z in zahlen if z % 2 == 0]
print(nur_gerade)


# Auswertungsreihenfolge der Operatoren (von hoch nach niedrig):
#  1. ()                         Klammern
#  2. **                         Potenz (rechtsassoziativ)
#  3. +x, -x, ~x                 Vorzeichen
#  4. *, /, //, %                Punktrechnung
#  5. +, -                       Strichrechnung
#  6. <<, >>                     Bitverschiebung
#  7. &                          bitweises UND
#  8. ^                          bitweises XOR
#  9. |                          bitweises ODER
# 10. ==, !=, <, >, <=, >=, in, not in, is, is not   Vergleiche
# 11. not                        logisches NICHT
# 12. and                        logisches UND
# 13. or                         logisches ODER
# 14. x if bedingung else y      bedingter Ausdruck
# 15. lambda
# 16. :=                         Walross-Operator
# Gleiche Stufe wird von links nach rechts ausgewertet (außer **).

print(2 + 3 * 4)        # 14, Punkt vor Strich
print((2 + 3) * 4)      # 20, Klammern zuerst
print(2 ** 3 ** 2)      # 512, rechts zuerst: 2 ** 9
print(-2 ** 2)          # -4, ** bindet stärker als das Minus
print(10 - 4 - 3)       # 3, links nach rechts: (10 - 4) - 3
print(1 < 3 < 5)        # True, Vergleichskette: 1 < 3 and 3 < 5
print(not 1 == 2)       # True, == vor not: not (1 == 2)
print(True or False and False)  # True, and vor or
