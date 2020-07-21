class Node:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
    
    def insert(self, value):
        if self.value == value:
            return False
        elif self.value > value:
            if self.leftNode:
                return self.leftNode.insert(value)
            else:
                self.leftNode = Node(value)
        else:
            if self.rightNode:
                return self.rightNode.insert(value)
            else:
                self.rightNode = Node(value)
                return True
    
    def find(self, value):
        if self.value == value:
            return True
        elif self.value > value:
            if self.leftNode:
                return self.leftNode.find(value)
            else:
                return False
        else:
            if self.rightNode:
                return self.rightNode.find(value)
            else:
                return False

    def pre_order(self):
        if self:
            print(self.value)
            if self.leftNode:
                self.leftNode.pre_order()
            if self.rightNode:
                self.rightNode.pre_order()

    def post_order(self):
        if self:
            if self.leftNode:
                self.leftNode.pre_order()
            if self.rightNode:
                self.rightNode.pre_order()
            print(self.value)

    def in_order(self):
        if self:
            if self.leftNode:
                self.leftNode.pre_order()
            print(self.value)
            if self.rightNode:
                self.rightNode.pre_order()


class Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root:
            return self.root.insert(value)
        else:
            self.root = Node(value)
            return True

    def find(self, value):
        if self.root:
            return self.root.find(value)
        else:
            return False

    def pre_order(self):
        print("Pre Order")
        self.root.pre_order()

    def post_order(self):
        print("Post Order")
        self.root.post_order()

    def in_order(self):
        print("In Order")
        self.root.in_order()

bst = Tree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(9)
bst.insert(9)
'''bst.pre_order()
bst.post_order()
bst.in_order()'''
