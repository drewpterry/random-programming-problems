import unittest

# check if brackets are correctly nested
def bracket_validator(s):
    brackets = {
            '{': '}',
            '(': ')',
            '[': ']',
            }
    openers = frozenset(brackets.keys())
    closers = frozenset(brackets.values())
    bracket_stack = [] 
    for char in s:
        if char in openers:
            bracket_stack.append(char)
        if char in closers:
            last_bracket = bracket_stack.pop()
            if char != brackets[last_bracket]:
                return False

    if len(bracket_stack) == 0:
        return True
    
class Test(unittest.TestCase):

    def test_reverses_words(self):
        self.assertEqual(True, bracket_validator('({[]})'))
        self.assertEqual(False, bracket_validator('({[}])'))

if __name__ == "__main__":
    unittest.main()
