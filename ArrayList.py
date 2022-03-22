import random
import time


class ArrayList:

    def __init__(self):
        self.list = []

    def insertStart(self, neueDaten):
        self.list.insert(0, neueDaten)

    def insertEnd(self, neueDaten):
        self.list.append(neueDaten)

    def length(self):
        return len(self.list)

    def insertionSort(self):
        for i in range(1, len(self.list)):

            key = self.list[i]
            j = i - 1
            while j >= 0 and key < self.list[j]:
                self.list[j + 1] = self.list[j]
                j -= 1
            self.list[j + 1] = key

    def findByIndex(self, index):
        if self.list is None:
            print("Liste ist leer")
        else:
            return self.list[index]


def Main():
    a1 = ArrayList()

    anzahl = int(input("Anzahl der Elemente die erzeugt werden sollen: "))
    if anzahl > 0:
        for i in range(0, anzahl):
            i = random.randint(0, anzahl)
            a1.insertEnd(i)
        print("\n")

    start = time.time()
    a1.insertionSort()
    end = time.time()

    print(a1.list)

    print("\n")
    print("Zeit für Insertion Sort: {:5.3f}s".format(end - start))


if __name__ == "__main__":
    Main()
