import unittest

def palindrome(s):
    seen_char = set()
    for char in s:
        if char in seen_char:
            seen_char.remove(char)
        else:
            seen_char.add(char)

    return len(seen_char) <= 1

class Test(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(True, palindrome('aabbccd'))
        self.assertEqual(False, palindrome('(aabbgh'))

if __name__ == "__main__":
    unittest.main()
