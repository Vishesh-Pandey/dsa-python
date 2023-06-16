
class Queue:
    def __init__(self):
        self.elements = [] 

    def size(self):
        return len(self.elements)

    def enqueue(self , data):
        self.elements.append(data)

    def dequeue(self):
        if self.size() == 0 :
            return "underflow"
        
        return self.elements.pop(0)

    def peek(self):
        if self.size() == 0 :
            return "underflow"
        
        return self.elements[0]
    
queue = Queue()
queue.enqueue(8)
queue.enqueue(7)

print("Size :" , queue.size())
print("Peek :" , queue.peek())

print("All elements :" , queue.elements)

queue.dequeue()

print("All elements :" , queue.elements)

