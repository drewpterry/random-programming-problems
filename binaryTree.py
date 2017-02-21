class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def setNodeValue(self, value):
        self.value = value

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)

# tree = BinaryTreeNode(5)
# tree.insert_left(4)
# tree.left.insert_left(1)
# tree.left.insert_right(0)
# tree.insert_right(3)
# tree.right.insert_right(6)
# tree.right.insert_left(2)

# def printTree(tree):
    # if tree != None:
        # printTree(tree.left)
        # print(tree.value)
        # printTree(tree.right)

# printTree(tree)
