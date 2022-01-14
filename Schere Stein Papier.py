import random

spieler_wahl = 0
computer_wahl = 0
computer_punkte = 0
spieler_punkte = 0
status = 0
spiel = 1

while spiel == 1:
    while status == 0:
        print(""
              "")
        print("Deine Punkte: " + str(spieler_punkte))
        print("Computer Punkte: " + str(computer_punkte))
        spieler_wahl = (int(input("Schere [1], Stein [2] oder Papier [3]: ")))
        computer_wahl = random.randrange(1, 4)
        status = 1
    #Überprüfung
    if status == 1:
        #Unentschieden
        if spieler_wahl == computer_wahl:
            print("Unentschieden :)")
        #Schere
        elif spieler_wahl == 1:
            if computer_wahl == 2:
                print("Verloren, Computer gewinnt mit Stein gegen Schere")
                computer_punkte = computer_punkte + 1
            elif computer_punkte == 3:
                print("Gewonnen, Computer verliert Papier gegen Schere")
                spieler_punkte = spieler_punkte + 1
        #Stein
        elif spieler_wahl == 2:
            if computer_wahl == 1:
                print("Gewonnen, Computer verliert mit Schere gegen Stein")
                spieler_punkte = spieler_punkte + 1
            elif computer_wahl == 3:
                print("Verloren, Computer gewinnt mit Papier gegen Stein")
                computer_punkte = computer_punkte + 1
        #Papier
        elif spieler_wahl == 3:
            if computer_wahl == 1:
                print("Verloren, Computer gewinnt mit Schere gegen Papier")
                computer_punkte = computer_punkte + 1
            elif computer_wahl == 2:
                print("Gewonnen, Computer verliert mit Stein gegen Papier")
                spieler_punkte = spieler_punkte + 1
        status = 0

datei = open('Textdatei.txt', 'w')
datei.write("weitere Zeile")
datei.close()