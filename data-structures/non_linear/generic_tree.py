
class TreeNode:
    def __init__(self , data):
        self.data = data 
        self.parent = None 
        self.childrens = [] 

    def addChild(self , child):
        child.parent = self 
        self.childrens.append(child)

    def getLevel(self):
        level = 0 

        parent = self.parent 

        while parent : 
            level += 1 
            parent = parent.parent 

        return level 

    def display(self):
        if self.getLevel() == 0 :
            print(self.data)
        else:
            print("  "*self.getLevel()+"|___" , self.data)
        if self.childrens:
            for child in self.childrens:
                child.display()


desktop = TreeNode("Desktop")

games = TreeNode("Games")
programming = TreeNode("Programming")

python = TreeNode("python")
react = TreeNode("react")

minecraft = TreeNode("minecraft")

games.addChild(minecraft)

desktop.addChild(games)
desktop.addChild(programming)

programming.addChild(python)
programming.addChild(react)

desktop.display()