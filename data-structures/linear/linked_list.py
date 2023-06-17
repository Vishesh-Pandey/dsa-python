
class Node:
    def __init__(self , data):
        self.data = data
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def addAtBeginning(self , data ):
        node = Node(data)
        node.next = self.head
        self.head = node 

    def addAtEnd(self , data ):
        ptr = self.head 

        while ptr.next:
            ptr = ptr.next 

        ptr.next = Node(data)

    def removeFromBeginning(self):
        self.head = self.head.next 

    def removeFromEnd(self):
        ptr = self.head 

        while ptr.next.next:
            ptr = ptr.next 
        
        ptr.next = None 

    def size(self):
        ptr = self.head 
        
        length = 0 

        while ptr:
            length += 1 
            ptr = ptr.next 

        return length

    def addAt(self , data , index):
        if self.size() < index : 
            return 
        
        elif index == 0 :
            self.addAtBeginning(data)

        elif index == self.size():
            self.addAtEnd(data)
        
        ptr = self.head
        currentIndex = 0 

        while currentIndex <= index:
            if currentIndex == index - 1:
                node = Node(data)
                node.next = ptr.next
                ptr.next = node 
                break

    def display(self):
        ptr = self.head 
        while ptr:
            print(ptr.data , end=" --> ")
            ptr = ptr.next 
        print()


linkedList = LinkedList()

linkedList.addAtBeginning(8)
linkedList.addAtBeginning(4)

linkedList.addAtEnd(2)

linkedList.addAt(5,1)

linkedList.display()

linkedList.removeFromBeginning()
linkedList.removeFromEnd()

print(linkedList.size())

linkedList.display()