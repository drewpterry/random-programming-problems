import unittest

#O(n) or O(1)
def is_unique_char(string):
    if len(string) > 128:
        return False
    char_set = {}
    for character in string:
        try:
            char_set[character]
            return False
        except:
            char_set[character] = True
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = is_unique_char(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = is_unique_char(test_string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
