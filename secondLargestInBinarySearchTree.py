from binaryTree import BinaryTreeNode
def second_largest_in_binary_search_tree(tree_node):
    current_second_largest = tree_node
    left_subtree = tree_node
    node = tree_node
    final_found = False
    while final_found == False:
        if node.right:
            current_second_largest = node.value
            node = node.right
        else:
            if node.left:
                current_second_largest if current_second_largest > node.left.value else node.left.value
            final_found = True
        
    return current_second_largest 

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
print second_largest_in_binary_search_tree(tree)
