import time
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


def swapData(first, second):
    value = first.data
    first.data = second.data
    second.data = value


class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

    def addbeginning(self, data):
        if self.head is None:
            new_Node = Node(data)
            new_Node.prev = None
            self.head = new_Node
        else:
            new_Node = Node(data)
            self.head.prev = new_Node
            new_Node.next = self.head
            self.head = new_Node
            new_Node.prev = None

    def print(self):
        current = self.head

        if self.head is None:
            print("List is empty")

        while current:
            print(current.data)
            current = current.next

    def add_after_node(self, key, data):
        current = self.head
        while current:
            if current.next is None and current.data == key:
                self.add(data)
                return
            elif current.data == key:
                new_node = Node(data)
                nxt = current.next
                current.next = new_node
                new_node.next = nxt
                new_node.prev = current
                nxt.prev = new_node
            current = current.next

    def add_before_node(self, key, data):
        current = self.head
        while current:
            if current.prev is None and current.data == key:
                self.addbeginning(data)
                return
            elif current.data == key:
                new_node = Node(data)
                prev = current.prev
                prev.next = new_node
                current.prev = new_node
                new_node.next = current
                new_node.prev = prev
            current = current.next

    def delete(self, key):
        current = self.head
        while current:
            if current.data == key and current == self.head:

                if not current.next:
                    current = None
                    self.head = None
                    return

                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return

            elif current.data == key:

                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current = None
                    return

                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next

    def length(self):
        if self.head is None:
            print("DoublyLinkedList is Empty!")
        else:
            res = 0
            while self.head is not None:
                res = res + 1
                self.head = self.head.next
            return res

    def insertionSortAsc(self):
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data < back.prev.data:
                swapData(back, back.prev)
                back = back.prev

            front = front.next

    def insertionSortDesc(self):
        front = self.head
        back = None
        while front is not None:
            back = front.next
            while back is not None and back.prev is not None and back.data > back.prev.data:
                swapData(back, back.prev)
                back = back.prev

            front = front.next

    def searchNode(self, value):
        i = 1
        flag = False
        current = self.head

        if self.head is None:
            print("List is empty")
            return

        while current is not None:
            if current.data == value:
                flag = True
                break
            current = current.next
            i = i + 1

        if flag:
            print("Das gesuchte Element ist in dieser Position vorhanden: " + str(i))
        else:
            print("Das gesuchte Element ist nicht vorhanden")


def Main():
    dl = DoubleLinkedList()

    anzahl = int(input("Anzahl der Elemente die erzeugt werden sollen: "))
    if anzahl > 0:
        s = time.time()
        for i in range(0, anzahl):
            i = random.randint(0, anzahl)
            dl.add(i)
        e = time.time()
        print("\n")
    # dl.add(6) # search (6)
    print("Without Insertion Sort: ")
    dl.print()
    print("\n")

    start = time.time()
    dl.insertionSortAsc()
    end = time.time()

    print("\n")
    print("With Insertion Sort: ")
    dl.print()

    print("\n")
    print("Zeit für Insertion Sort: {:5.5f}s".format(end - start))
    print("Zeit für befüllen der List: {:5.3f}s".format(e - s))
    print("-----------------------------------------------------")

    print("\n")
    # dl.searchNode(6)
    print("Length of the List: " + str(dl.length()))


if __name__ == "__main__":
    Main()
