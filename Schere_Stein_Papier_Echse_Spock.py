import random

computer = 0
spieler = 0

auswahl_liste = {1: "Schere", 2: "Papier", 3: "Stein", 4: "Echse", 5: "Spock"}
win = ("----DU HAST GEWONNEN!----")
loose = ("----DU HAST VERLOREN!----")

while True:
    print("1 - Schere   2 - Papier   3 - Stein   4 - Echse   5 - Spock \n")

    d = int(input("Deine Wahl(1-5): "))
    print("-> ", auswahl_liste[d])
    #print("Deine Punkte: " + str(spieler), "\n")

    print("Computer Wahl(1-5): ")
    e = random.randrange(1, 6)
    print("-> ", auswahl_liste[e])
    #print("Computer Punkte: ", str(computer), "\n")

    # Schere
    if d == 1 and (e == 2 or e == 4):
        print(win)
        spieler = spieler + 1

    elif (d == 2 or d == 4) and e == 1:
        print(loose)
        computer = computer + 1

    # Papier
    elif d == 2 and (e == 3 or e == 5):
        print(win)
        spieler = spieler + 1
    elif (d == 3 or d == 5) and e == 2:
        print(loose)

    # Stein
    elif d == 3 and (e == 4 or e == 1):
        print(win)
        spieler = spieler + 1
    elif (d == 4 or d == 1) and e == 3:
        print(loose)
        computer = computer + 1

    # Echse
    elif d == 4 and (e == 5 or e == 2):
        print(win)
        spieler = spieler + 1
    elif (d == 5 or d == 2) and e == 4:
        print(loose)
        computer = computer + 1

    # Spock
    elif d == 5 and (e == 1 or e == 3):
        print(win)
        spieler = spieler + 1
    elif (d == 1 or d == 3) and e == 5:
        print(loose)
        computer = computer + 1
    else:
        print("----GLEICHSTAND!----")
    print("\n")

    nochmal = input("Wollen sie nochmal spielen? [j / n]: ")
    if nochmal == "n":
        break

# Daten in eine .txt Datei einlesen
file = open("Textdatei.txt", "w")

file.write("Ergbenisse vom Spieler: " + str(spieler))
file.write("\n")
file.write("Ergebnisse vom Computer: " + str(computer))
file.write("\n")
file.write("So oft wurde gespielt: ")

file.close()