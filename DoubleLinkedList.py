class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

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
                # Fall 1
                if not current.next:
                    current = None
                    self.head = None
                    return

                # Fall 2
                else:
                    nxt = current.next
                    current.next = None
                    nxt.prev = None
                    current = None
                    self.head = nxt
                    return

            elif current.data == key:
                # Fall 3
                if current.next:
                    nxt = current.next
                    prev = current.prev
                    prev.next = nxt
                    nxt.prev = prev
                    current.next = None
                    current = None
                    return

                # Fall 4
                else:
                    prev = current.prev
                    prev.next = None
                    current.prev = None
                    current = None
                    return
            current = current.next


# Durchführung

dl = DoubleLinkedList()

dl.add(1)
dl.add(2)
dl.add(3)
dl.add(4)

dl.add_before_node(1, 0)
dl.add_after_node(4, 5)
dl.delete(0)

dl.print()