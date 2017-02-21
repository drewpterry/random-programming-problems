import unittest

def rotation_point(array):
    first_word = array[0]
    floor_index = 0
    ceiling_index = len(array) - 1
    
    while floor_index < ceiling_index:
        guess = floor_index + ((ceiling_index - floor_index)/2)

        if first_word < array[guess]:
            floor_index = guess
        else:
            ceiling_index = guess

        if floor_index + 1  == ceiling_index:
            return ceiling_index

class Test(unittest.TestCase):
    words = [
        'ptolemaic',
        'retrograde',
        'supplant',
        'undulate',
        'vndulate',
        'vpdulate',
        'xenoepist',
        'asymptote', # <-- rotates here!
        'babka',
        'banoffee',
        'engender',
        'karpatka',
        'othellolagkage',
    ]
    def test_cp(self):
        self.assertEqual(7,rotation_point(self.words))

if __name__ == "__main__":
    unittest.main()
