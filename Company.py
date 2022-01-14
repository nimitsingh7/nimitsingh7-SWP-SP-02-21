import CompanyClasses

if __name__ == "__main__":

    # Mitarbeiter erzeugen
    m1 = CompanyClasses.Mitarbeiter("Nimit", "Singh", 21, 1, "Verkaufsleiter", 1900)
    m2 = CompanyClasses.Mitarbeiter("Ina", "Masunic", 22, 2, "Programmierer", 2000)
    m3 = CompanyClasses.Mitarbeiter("Martin", "Schatz", 19, 1, "Verkäufer", 1800)

    # Gruppenleiter erzeugen
    g1 = CompanyClasses.Gruppenleiter("Sabo", "Rubner", 25, 1)
    g2 = CompanyClasses.Gruppenleiter("Max", "Neuner", 19, 1)

    # Liste mit allen Personen befüllen
    allpersonen = []
    allpersonen.append(m1)
    allpersonen.append(m2)
    allpersonen.append(m3)
    allpersonen.append(g1)
    allpersonen.append(g2)

    # Abteilungen erzeugen
    a1 = CompanyClasses.Abteilungen("Einkauf")
    a1.leiter.append(g1)
    a1.Worker.append(m1)

    a2 = CompanyClasses.Abteilungen("Verkauf")
    a2.leiter.append(g2)
    a2.Worker.append(m2)
    a2.Worker.append(m3)

    a3 = CompanyClasses.Abteilungen("Vertrieb")

    # Company erzeugen
    c1 = CompanyClasses.Company("Company1")
    c1.Abteilung.append(a1)
    c1.Abteilung.append(a2)
    c1.Abteilung.append(a3)

    c1.printAbteilungen()

    def countMitarbeiter(Worker):
        return len(Worker)

    def countGruppenleiter(leiter):
        return len(leiter)

    def countAbteilungen(Abteilung):
        return len(Abteilung)

    def GenderMalePercentage():
        maleP = [x for x in allpersonen if x.gender == 1]
        return len(maleP) / len(allpersonen)

    print("Gender Male Percentage in the Company: ")
    print(GenderMalePercentage())

    print("Gender Women Percentage in the Company: ")
    print(1 - GenderMalePercentage())
    print("\n")

    print("Anzahl der Mitarbeiter in der Abteilung " + str(a2))
    print(countMitarbeiter(a2.Worker))
    print("\n")
    print("Anzahl der Gruppenleiter in jeder Abteilung: ")
    print(countGruppenleiter(a1.leiter))
    print(countGruppenleiter(a2.leiter))
    print("\n")
    print("Anzahl der Abteilungen: ")
    print(countAbteilungen(c1.Abteilung))
