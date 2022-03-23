import random
import time


class ArrayList:

    def __init__(self):
        self.list = []

    def addStart(self, newData):
        self.list.insert(0, newData)

    def addEnd(self, newData):
        self.list.append(newData)

    def addAfter(self, pos, data):
        self.list.insert(pos + 1, data)

    def addBefore(self, pos, data):
        if pos - 1 >= 0:
            self.list.insert(pos - 1, data)

    def delete(self, pos):
        self.list.pop(pos)

    def deleteAfter(self, pos):
        if len(self.list) > pos + 1:
            self.list.pop(pos + 1)

    def deleteBefore(self, pos):
        if pos - 1 >= 0:
            self.list.pop(pos - 1)

    def length(self):
        return len(self.list)

    def findByIndex(self, index):
        if self.list is None:
            print("Liste ist leer")
        else:
            return self.list[index]

    def sortAsc(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key

    def sortDesc(self):
        for i in range(1, len(self.list)):
            key = self.list[i]
            j = i - 1
            while j >= 0 and key > self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key


def Main():
    a1 = ArrayList()

    anzahl = int(input("Anzahl der Elemente die erzeugt werden sollen: "))
    if anzahl > 0:
        for i in range(0, anzahl):
            i = random.randint(0, anzahl)
            a1.addEnd(i)

    print("\n")
    print("List without Insertion Sort: ")
    print(a1.list)
    print("\n")

    print("List with Insertion Sort: ")
    start = time.time()
    a1.sortAsc()
    end = time.time()
    print(a1.list)

    print("\n")
    # print("Length of the List: " a1.length() "!")

    print("\n")
    print("Zeit für Insertion Sort: {:5.5f}s".format(end - start))


if __name__ == "__main__":
    Main()
