from enum import Enum

class Gender(Enum):
    male = 1
    female = 2

class Person:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age) + " " + str(self.gender)

class Mitarbeiter(Person):
    def __init__(self, firstname, lastname, age, gender, position, gehalt):
        super().__init__(firstname, lastname, age, gender)
        self.position = position
        self.gehalt = gehalt

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age) + " " + str(self.gender) + " " + self.position + " " + str(self.gehalt)

class Gruppenleiter:
    def __init__(self, firstname, lastname, age, gender):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age) + " " + str(self.gender)

class Abteilungen:
    def __init__(self, name):
        self.name = name
        self.Worker = []
        self.leiter = []

    def __str__(self):
        return self.name

class Company:
    def __init__(self, cname):
        self.cname = cname
        self.Abteilung = []

    def printAbteilungen(self):
        for a in self.Abteilung:
            print(a)

    def __str__(self):
        return self.cname