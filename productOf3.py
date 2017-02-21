#Given a list_of_ints, find the highest_product you can get from three of the integers
import unittest

#O(n log n) because of sort
def largest_product_of_three(array):
    array.sort()
    length = len(array)
    highest = array[length - 1]
    second_highest = array[length - 2]
    third_highest = array[length - 3]
    lowest = array[0]
    lowest_second = array[1]

    positive_high = second_highest * third_highest
    negative_high = lowest * lowest_second

    highest_check = highest * positive_high
    lowest_check  = highest * negative_high
    product = max(highest_check, lowest_check) 
    return product

# O(n)
def largest_product_of_three_greedy(array):
    length = len(array)
    highest = max(array[0], array[1])
    product_of_highest_two = array[0] * array[1]
    product_of_highest_three = array[0] * array[1] * array[2]
    lowest = min(array[0], array[1])
    product_of_lowest_two = array[0] * array[1]

    for index, each in enumerate(array):
        if index > 1:
            #order that you set variables is important
            highest_product_of_3 = max(
                highest_product_of_3,
                current * highest_product_of_2,
                current * lowest_product_of_2)

            highest_product_of_2 = max(
                highest_product_of_2,
                current * highest,
                current * lowest)

            lowest_product_of_2 = min(
                lowest_product_of_2,
                current * highest,
                current * lowest)

            highest = max(highest, current)

            lowest = min(lowest, current)
    return product_of_highest_three 

class Test(unittest.TestCase):

    def test(self):
        self.assertEqual(84, largest_product_of_three([1,7,3,4]))
        self.assertEqual(-12, largest_product_of_three([-1,-7,-3,-4]))
        self.assertEqual(21, largest_product_of_three([-1,7,-3,4]))

if __name__ == "__main__":
    unittest.main()
