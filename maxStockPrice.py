# given array of stock prices find the maximum profit you can make, the array is in time order
# so you cannot sell a stock before you buy one:

import unittest
def get_max_profit(yesterday_prices):
    max_price = yesterday_prices[1] - yesterday_prices[0]
    lowest = yesterday_prices[0]
    for index, each in enumerate(yesterday_prices):
        if each - lowest > max_price:
            if index != 0:
                max_price = each - lowest
        if each < lowest:
            lowest = each
    return max_price

class Test(unittest.TestCase):
    data = [10, 11, 7, 5, 8, 11, 9]
    data_decreasing = [10, 5, 4, 3, 2]
    data_no_change = [5, 5, 5, 5, 5]

    def test_cp(self):
        max_profit = get_max_profit(self.data)
        self.assertEqual(max_profit, 6)

        max_profit = get_max_profit(self.data_decreasing)
        self.assertEqual(max_profit, -1)

        max_profit = get_max_profit(self.data_no_change)
        self.assertEqual(max_profit, 0)

if __name__ == "__main__":
    unittest.main()
