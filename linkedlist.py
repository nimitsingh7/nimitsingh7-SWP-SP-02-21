class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    head = None

    def __init__(self):
        self.head = None

    def printList(self):
        current = self.head

        while current is not None:
            print(" - node: {0}\n - content: {1}\n - next node at: {2}\n".format(current, current.data, current.next))
            current = current.next

        print()

    def addToList(self, newData):
        newNode = Node(newData)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = newNode


    def removeFromList(self, removeKey):
        headValue = self.head

        if headValue is not None:
            if headValue.data == removeKey:
                self.head = headValue.next
                headValue = None
            else:
                previousNode = None

                while headValue is not None:
                    if headValue.data == removeKey:
                        break

                    previousNode = headValue
                    headValue = headValue.next

                if headValue is not None:
                    previousNode.next = headValue.next
                    headValue = None


    def reverseList(self):
        previousNode = None
        tmp = None
        currentNode = self.head

        while currentNode is not None:
            tmp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = tmp

        self.head = previousNode

    def clearList(self):
        current = self.head

        while current is not None:
            current = current.next
            del self.head
            self.head = current