# Übung 1: Python-Basics
# Kontrollstrukturen, bedingte Ausdrücke und match-case (je ein Beispiel)


# ---------------------------------------------------------------
# 1. Kontrollstrukturen
# ---------------------------------------------------------------

def beispiel_if():
    """if / elif / else: je nach Bedingung wird ein anderer Zweig ausgeführt."""
    temperatur = 23
    if temperatur > 30:
        print("if: Es ist heiß.")
    elif temperatur > 15:
        print("if: Es ist angenehm.")
    else:
        print("if: Es ist kalt.")


def beispiel_for():
    """for-Schleife: läuft über jedes Element einer Sequenz."""
    faecher = ["SWP", "Mathe", "Deutsch"]
    for fach in faecher:
        print(f"for: Heute habe ich {fach}.")


def beispiel_while():
    """while-Schleife: läuft, solange die Bedingung wahr ist."""
    countdown = 3
    while countdown > 0:
        print(f"while: {countdown} ...")
        countdown -= 1
    print("while: Start!")


def beispiel_break():
    """break: beendet die Schleife sofort."""
    zahlen = [4, 8, 15, 16, 23, 42]
    for zahl in zahlen:
        if zahl > 15:
            print(f"break: {zahl} ist die erste Zahl größer als 15, Schleife endet.")
            break
        print(f"break: {zahl} ist noch nicht größer als 15.")


def beispiel_continue():
    """continue: überspringt den Rest des aktuellen Durchlaufs."""
    for i in range(1, 7):
        if i % 2 == 0:
            continue
        print(f"continue: {i} ist ungerade.")


def beispiel_pass():
    """pass: Platzhalter, der nichts tut (z.B. für noch leere Blöcke)."""
    for i in range(3):
        if i == 1:
            pass  # hier soll später noch etwas passieren
        else:
            print(f"pass: i = {i}")

    class NochLeer:
        pass  # leere Klasse ist ohne pass ein Syntaxfehler

    print(f"pass: Leere Klasse erstellt: {NochLeer.__name__}")


def beispiel_try_except():
    """try-except: fängt Fehler ab, statt das Programm abstürzen zu lassen."""
    eingaben = ["10", "abc", "0"]
    for text in eingaben:
        try:
            ergebnis = 100 / int(text)
        except ValueError:
            print(f"try-except: '{text}' ist keine Zahl.")
        except ZeroDivisionError:
            print("try-except: Division durch 0 ist nicht erlaubt.")
        else:
            print(f"try-except: 100 / {text} = {ergebnis}")
        finally:
            print("try-except: finally wird immer ausgeführt.")


# ---------------------------------------------------------------
# 2. Bedingte Ausdrücke (Rheinwerk Openbook, Kapitel 5.1)
#    Syntax: wert_wenn_wahr if bedingung else wert_wenn_falsch
# ---------------------------------------------------------------

def beispiel_bedingter_ausdruck():
    """Ein if-else in einer Zeile, das einen Wert liefert."""
    alter = 17
    status = "volljährig" if alter >= 18 else "minderjährig"
    print(f"bedingter Ausdruck: Mit {alter} ist man {status}.")

    # Auch mitten in anderen Ausdrücken verwendbar:
    for zahl in range(1, 5):
        print(f"bedingter Ausdruck: {zahl} ist {'gerade' if zahl % 2 == 0 else 'ungerade'}")


# ---------------------------------------------------------------
# 3. Switch-Case in Python (DataCamp-Tutorial)
#    Seit Python 3.10 gibt es dafür match-case.
# ---------------------------------------------------------------

def wochentag_match(nummer):
    """match-case: vergleicht einen Wert mit mehreren Mustern."""
    match nummer:
        case 1:
            return "Montag"
        case 2:
            return "Dienstag"
        case 3:
            return "Mittwoch"
        case 4:
            return "Donnerstag"
        case 5:
            return "Freitag"
        case 6 | 7:  # mehrere Werte in einem case
            return "Wochenende"
        case _:  # Default, wie 'default' in anderen Sprachen
            return "ungültige Nummer"


def wochentag_dict(nummer):
    """Klassische Alternative vor Python 3.10: ein Dictionary als Switch."""
    tage = {1: "Montag", 2: "Dienstag", 3: "Mittwoch", 4: "Donnerstag", 5: "Freitag"}
    return tage.get(nummer, "Wochenende oder ungültig")


def beispiel_switch_case():
    for n in [1, 3, 6, 9]:
        print(f"match-case: {n} -> {wochentag_match(n)}")
    print(f"dict-switch: 2 -> {wochentag_dict(2)}")


if __name__ == "__main__":
    beispiele = [
        beispiel_if,
        beispiel_for,
        beispiel_while,
        beispiel_break,
        beispiel_continue,
        beispiel_pass,
        beispiel_try_except,
        beispiel_bedingter_ausdruck,
        beispiel_switch_case,
    ]
    for beispiel in beispiele:
        print(f"\n=== {beispiel.__name__} ===")
        beispiel()
