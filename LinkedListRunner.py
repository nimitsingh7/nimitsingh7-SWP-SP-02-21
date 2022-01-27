from linkedlist import LinkedList

def main():
    linkedlist = LinkedList()

    linkedlist.addToList(10)
    linkedlist.addToList(20)
    linkedlist.addToList(30)
    linkedlist.addToList(40)
    linkedlist.addToList(50)
    linkedlist.addToList(60)
    linkedlist.addToList(70)
    linkedlist.printList()

    print("removing an element from the List...")
    linkedlist.removeFromList(10)
    linkedlist.printList()

    linkedlist.addToList(10)

    print("reversing linked List...")
    linkedlist.reverseList()
    linkedlist.printList()

    linkedlist.clearList()

if __name__ == '__main__':
    main()