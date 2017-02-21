# O(log n)
import unittest

def binary_search(target, array):
    floor_index =  0 
    ceiling_index = len(array)
    while floor_index + 1 < ceiling_index:
        distance = ceiling_index - floor_index 
        midway_index = distance / 2
        guess_index = floor_index + midway_index
        guess_value = array[guess_index]
        if guess_value  == target:
            return guess_index
        elif target < guess_value:
            ceiling_index = guess_index 
        elif target > guess_value:
            floor_index = guess_index 
    return False 

class Test(unittest.TestCase):
    standard_array = [3,5,6,8,23,55,66]
    even_array = [3,5,6,8,23,55,66,74]
    negative_array = [-4,3,5,6,8,23,55,66,74]

    def test_cp(self):
        self.assertEqual(5,binary_search(55, self.standard_array))
        self.assertEqual(6,binary_search(66, self.standard_array))
        self.assertEqual(0,binary_search(3, self.standard_array))
        self.assertEqual(5,binary_search(55, self.even_array))
        self.assertEqual(0,binary_search(3, self.even_array))
        self.assertEqual(0,binary_search(-4, self.negative_array))
        # # false check
        self.assertFalse(binary_search(7, self.standard_array))
        self.assertFalse(binary_search(7, self.even_array))

if __name__ == "__main__":
    unittest.main()
