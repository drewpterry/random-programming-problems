# O(N)
import unittest

def check_permutation(string, string2):
    return sorted(string) == sorted(string2) ? true : false

class Test(unittest.TestCase):
    dataT = [(['abcd', 'bacd']), (['3563476', '7334566']),
             (['wef34f', 'wffe34'])]
    dataF = [(['abcd', 'd2cba']), (['2354', '1234']), (['dcw4f', 'dcw5f']),(['aBc', 'abc'])]

    def test_cp(self):
        # true check
        for test_string in self.dataT:
            actual = check_permutation(test_string[0], test_string[1])
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = check_permutation(test_string[0], test_string[1])
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()
