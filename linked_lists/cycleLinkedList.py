# check if linked list has a cycle
import pdb
import unittest
class LinkedListNode:
    
    def __init__(self, value):
      self.value = value
      self.next = None


# o(n) space complexity
def contains_cycle(node):
    seen_nodes = set()
    current_node = node
    while current_node is not None:
        if current_node not in seen_nodes:
            seen_nodes.add(node)
            current_node = current_node.next
        else:
            return True
    return False

# O(1) space complexity
def contains_cycle_using_runners(first_node):

    # start both runners at the beginning
    slow_runner = first_node
    fast_runner = first_node

    # until we hit the end of the list
    while fast_runner is not None and fast_runner.next is not None:
        slow_runner = slow_runner.next
        fast_runner = fast_runner.next.next

        # case: fast_runner is about to "lap" slow_runner
        if fast_runner is slow_runner:
            return True

    # case: fast_runner hit the end of the list
    return False
    

class Test(unittest.TestCase):
    first = LinkedListNode('A')
    second = LinkedListNode('B')
    third = LinkedListNode('C')
    fourth = LinkedListNode('D')

    def test_has_cycle(self):
        self.first.next = self.second 
        self.second.next = self.third 
        self.third.next = self.first
        self.assertEqual(True, contains_cycle(self.first))

    def test_has_no_cycle(self):
        self.first.next = self.second 
        self.second.next = self.third 
        self.third.next = self.fourth
        self.assertEqual(False, contains_cycle(self.first))

if __name__ == "__main__":
    unittest.main()
