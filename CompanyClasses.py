from enum import Enum

class Gender(Enum):
    male = True
    female = True

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age)

class Mitarbeiter(Person):
    def __init__(self, firstname, lastname, age, position, gehalt):
        super().__init__(firstname, lastname, age)
        self.position = position
        self.gehalt = gehalt

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age) + " " + self.position + " " + str(self.gehalt)

class Gruppenleiter(Mitarbeiter):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def __str__(self):
        return self.firstname + " " + self.lastname + " " + str(self.age)

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

    def __str__(self):
        return  self.cname