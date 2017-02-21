# O(N)
import unittest

#brute force O(n2)
def get_product_of_all_ints_except_at_index(array):
    products = []
    for index, each in enumerate(array):
        product = 1
        for index2, second in enumerate(array):
            if index != index2:
                product *= second
        products.append(product)
    return products

# better:  O(n)
def get_product_of_all_ints_except_at_index2(array):
    products = [None] * len(array)
    before_index = []
    after_index = [None] * len(array)
    product = 1
    for each in array:
        before_index.append(product)
        product *= each

    product = 1
    i = len(array) - 1
    while i >= 0:
        after_index[i] = product
        total = product * before_index[i]
        products[i] = total
        product *= array[i]
        i -= 1
    return products

class Test(unittest.TestCase):

    def test(self):
        self.assertListEqual([84,12,28,21], get_product_of_all_ints_except_at_index([1,7,3,4]))
        self.assertListEqual([84,12,28,21], get_product_of_all_ints_except_at_index2([1,7,3,4]))
        self.assertListEqual([0,0,0,0,84], get_product_of_all_ints_except_at_index2([1,7,3,4,0]))
        self.assertListEqual([1], get_product_of_all_ints_except_at_index2([5]))

if __name__ == "__main__":
    unittest.main()
