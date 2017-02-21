from binaryTree import BinaryTreeNode
def is_binary_search_tree(tree_node, lower_bound=-float('inf'), upper_bound=float('inf')):
    if not tree_node:
        return True
    if (tree_node.value > upper_bound) or (tree_node.value < lower_bound):
        return False
    return is_binary_search_tree(tree_node.left, lower_bound, tree_node.value) and is_binary_search_tree(tree_node.right, tree_node.value, upper_bound)

tree = BinaryTreeNode(6)
tree.insert_left(3)
tree.left.insert_left(1)
tree.left.insert_right(4)
tree.left.left.insert_left(0)
tree.left.left.left.insert_left(-1)
tree.insert_right(10)
tree.right.insert_right(11)
tree.right.insert_left(9)

#should return false
print is_binary_search_tree(tree)
