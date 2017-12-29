import unittest
class LinkedListNode:
    
    def __init__(self, value):
      self.value = value
      self.next = None

def delete_node(node):
    next_node = node.next
    if next_node:
        node.value = next_node.value
        node.next = next_node.next
        return
    else:
        raise Exception("Can't delete the last node with this technique!")
    

class Test(unittest.TestCase):
    first = LinkedListNode('A')
    second = LinkedListNode('B')
    third = LinkedListNode('C')

    first.next = second 
    second.next = third 

    def test_deletes_node(self):
        self.assertEqual('B', self.first.next.value)
        delete_node(self.second)
        self.assertEqual('C', self.first.next.value)

    def test_throws_error_if_last_node(self):
        with self.assertRaises(Exception):
            delete_node(self.third)

if __name__ == "__main__":
    unittest.main()
