import unittest

# string and position of parenthesis
def closing_parenthesis(s, point):
    chars = list(s)[point:]
    print chars
    p_count = 0
    for i, char in enumerate(chars):
        if char == '(':
            p_count += 1
        elif char == ')':
            p_count -= 1
            if p_count == 0:
                return i

    return
    
# better not to take slice as it causes space to be O(n)
# can use while loop

class Test(unittest.TestCase):

    def test_closing_parenthesis(self):
        self.assertEqual(11, closing_parenthesis('(hello()llj) ljwer', 0))

if __name__ == "__main__":
    unittest.main()
