import unittest

class Fibonacci:
    def __init__(self):
        self.cache = {}

    def getFibonacci(self, index):
        if index == 0:
            return 0
        if index == 1:
            return 1
        if index in self.cache:
            return self.cache[index]
        result = self.getFibonacci(index - 1) + self.getFibonacci(index - 2)
        self.cache[index] = result 
        return result

class Test(unittest.TestCase):
    def test_cp(self):
        self.assertEquals(0,Fibonacci().getFibonacci(0))
        self.assertEquals(1,Fibonacci().getFibonacci(1))
        self.assertEquals(1,Fibonacci().getFibonacci(2))
        self.assertEquals(2,Fibonacci().getFibonacci(3))
        self.assertEquals(3,Fibonacci().getFibonacci(4))

if __name__ == "__main__":
    unittest.main()
