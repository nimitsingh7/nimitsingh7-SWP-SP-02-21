import CompanyClasses

if __name__ == "__main__":

    # Mitarbeiter erzeugen
    m1 = CompanyClasses.Mitarbeiter("Nimit", "Singh", 21, "Verkaufsleiter", 1900)
    m2 = CompanyClasses.Mitarbeiter("Phillip", "Schueler", 18, "Programmierer", 2000)

    # Gruppenleiter erzeugen
    g1 = CompanyClasses.Gruppenleiter("Sabo", "Rubner", 25)
    g2 = CompanyClasses.Gruppenleiter("Max", "Neuner", 19)

    # Abteilungen erzeugen
    a1 = CompanyClasses.Abteilungen("Einkauf")
    a1.leiter.append(g1)
    a1.Worker.append(m1)
    a2 = CompanyClasses.Abteilungen("Verkauf")
    a2.leiter.append(g2)
    a2.Worker.append(m2)

    a3 = CompanyClasses.Abteilungen("Vertrieb")

    # Company erzeugen
    c1 = CompanyClasses.Company("Company1")
    c1.Abteilung.append(a1)
    c1.Abteilung.append(a2)
    c1.Abteilung.append(a3)

    def countMitarbeiter(Worker):
        return len(Worker)

    def countGruppenleiter(leiter):
        return len(leiter)

    def countAbteilungen(Abteilung):
        return len(Abteilung)

    print("Anzahl der Mitarbeiter in der Abteilung Einkauf: ")
    print(countMitarbeiter(a1.Worker))
    print("\n")
    print("Anzahl der Abteilungen: ")
    print(countAbteilungen(c1.Abteilung))
    print("\n")
    print("Anzahl der Gruppenleiter in jeder Abteilung: ")
    print(countGruppenleiter(a1.leiter))
    print(countGruppenleiter(a2.leiter))