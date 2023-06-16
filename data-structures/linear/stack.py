
class Stack: 
    def __init__(self):
        self.elements = [] 

    def size(self):
        return len(self.elements)

    def push(self , data ):
        self.elements.append(data)

    def pop(self):
        if self.size() == 0 :
            return "underflow"
        
        return self.elements.pop()
    
    def peek(self):
        if self.size == 0 :
            return "underflow"
        
        return self.elements[-1]
    
stack = Stack()

stack.push(8)
stack.push(7)

print("Size :" , stack.size())
print("Peek :" , stack.peek())

print("All elements :" , stack.elements)

stack.pop()

print("All elements :" , stack.elements)

