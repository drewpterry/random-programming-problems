import unittest
from random import Random

# fisher-yates shuffle
def shuffle(values):
    if len(values) <= 1:
        return values 

    floor = 0
    ceiling = len(values) - 1
    for i in range(0, ceiling):
        rand_val = get_random(i, ceiling)
        values[i], values[rand_val] = values[rand_val], values[i]

    return values


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)

class Test(unittest.TestCase):
    def setUp(self):
        global random
        random = Random(212)

    def test_shuffle(self):
        self.assertEqual([4,5,1], shuffle([1,4,5]))

if __name__ == "__main__":
    unittest.main()
