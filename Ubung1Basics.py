temperatur = 23
if temperatur > 30:
    print("heiß")
elif temperatur > 15:
    print("angenehm")
else:
    print("kalt")

for fach in ["SWP", "Mathe", "Deutsch"]:
    print(fach)

countdown = 3
while countdown > 0:
    print(countdown)
    countdown -= 1

for zahl in [4, 8, 15, 16, 23]:
    if zahl > 15:
        break
    print(zahl)

for i in range(3):
    if i == 1:
        pass
    else:
        print(i)

try:
    ergebnis = 100 / 0
except ZeroDivisionError:
    print("Division durch 0")

alter = 17
status = "volljährig" if alter >= 18 else "minderjährig"
print(status)

tag = 6
match tag:
    case 1:
        print("Montag")
    case 6 | 7:
        print("Wochenende")
    case _:
        print("anderer Tag")
