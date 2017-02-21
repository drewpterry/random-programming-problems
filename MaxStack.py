from stack import Stack 
import unittest

class MaxStack:
    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()

    def push(self, item):
        self.stack.push(item)
        if not self.maxs_stack.peek() or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()
        return item
        
    def get_max(self):
        return self.maxs_stack.peek()

class Test(unittest.TestCase):

    def test_cp(self):
        stack = MaxStack()
        stack.push(5)
        stack.push(3)
        stack.push(7)
        stack.pop()
        self.assertEqual(5,stack.get_max())

if __name__ == "__main__":
    unittest.main()
