import queue

class TreeNode:

    def __init__(self, number):
        self.value = number
        self.left = None
        self.right = None

    def printInOrder(self):
        if (self.left):
            self.left.printInOrder()
        print(self.value)
        if (self.right):
            self.right.printInOrder()

    def printPreOrder(self):
        print(self.value)
        if (self.left):
            self.left.printPreOrder()        
        if (self.right):
            self.right.printPreOrder()

    def printPostOrder(self):        
        if (self.left):
            self.left.printPostOrder()        
        if (self.right):
            self.right.printPostOrder()
        print(self.value)

    def printLevelOrder(self):
        q = queue.Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            print(node.value)
            if (node.left):
                q.put(node.left)
            if (node.right):
                q.put(node.right)   

node = TreeNode(1)
node.left = TreeNode(2)
node.right = TreeNode(3)
node.left.left = TreeNode(4)
node.left.right = TreeNode(5)

print ("Print Tree InOrder")
node.printInOrder()
print ("Print Tree PreOrder")
node.printPreOrder()
print ("Print Tree PostOrder")
node.printPostOrder()

print ("Print Tree Level Order")
node.printLevelOrder()