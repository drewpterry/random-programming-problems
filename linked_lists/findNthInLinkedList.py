import unittest
class LinkedListNode:
    
    def __init__(self, value):
      self.value = value
      self.next = None

def kth_to_last_node(k, head_node):
    current = head_node
    previous = None
    next = None

    while current:
        next = current.next
        current.next = previous
        previous = current
        current = next 
    return previous 
    

class Test(unittest.TestCase):
    first = LinkedListNode('A')
    second = LinkedListNode('B')
    third = LinkedListNode('C')
    fourth = LinkedListNode('D')
    fifth = LinkedListNode('E')

    def test_reverses_list(self):
        self.first.next = self.second 
        self.second.next = self.third 
        self.third.next = self.fourth
        self.fourth.next = self.fifth
        
        self.assertEqual('D', kth_to_last_node(2, self.first))

    def test_only_one_reverses_list(self):
        self.assertEqual('A', reverse_linked_list(self.first).value)

if __name__ == "__main__":
    unittest.main()
