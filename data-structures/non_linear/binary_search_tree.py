
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

    def addChild(self , data):
        if data == self.data :
            return 
        
        elif data < self.data :
            if self.left : 
                self.left.addChild(data)

            else:
                self.left = BinarySearchTreeNode(data)

        else:
            if self.right :
                self.right.addChild(data)

            else:
                self.right = BinarySearchTreeNode(data)

    def inOrderTraversal(self):
        elements = [] 

        if self.left : 
            elements.extend(self.left.inOrderTraversal())

        elements.append(self.data)

        if self.right : 
            elements.extend(self.right.inOrderTraversal())

        return elements 
    
    def preOrderTraversal(self):
        elements = [] 

        elements.append(self.data)

        if self.left : 
            elements.extend(self.left.preOrderTraversal())

        if self.right : 
            elements.extend(self.right.preOrderTraversal())

        return elements 
    
    def postOrderTraversal(self):
        elements = []

        if self.left : 
            elements.extend(self.left.postOrderTraversal())

        if self.right : 
            elements.extend(self.right.postOrderTraversal())

        elements.append(self.data)

        return elements 


rootNode = BinarySearchTreeNode(5)

rootNode.addChild(5)
rootNode.addChild(2)
rootNode.addChild(4)
rootNode.addChild(7)
rootNode.addChild(6)
rootNode.addChild(9)

print("in order traversal :" , rootNode.inOrderTraversal())
print("pre order traversal :" , rootNode.preOrderTraversal())
print("post order traversal :" , rootNode.postOrderTraversal())