import unittest
# returns the times a meeting is happening
def coin_output(amount, denominations):
    return

class CoinDenominator:
    def __init__(self):
        self.memo = {} 

    def change_possibilities_bottom_down(self, amount, denominations):
        ways_of_doing_n_cents = [0] * (amount + 1)
        ways_of_doing_n_cents[0] = 1

        for coin in denominations:
            print 'coin', coin
            for higher_amount in xrange(coin, amount + 1):
                print "higher amount", higher_amount
                higher_amount_remainder = higher_amount - coin
                print "higher amount remainder", higher_amount_remainder 
                ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]
                print ways_of_doing_n_cents

        print "result", ways_of_doing_n_cents[amount]
        return ways_of_doing_n_cents[amount]

    def change_possibilities_top_down(self, amount_left, denominations, current_index=0):

        memo_key = str((amount_left, current_index))
        if memo_key in self.memo:
            return memo[memo_key]
        # base cases:
        # we hit the amount spot on. yes!
        if amount_left == 0: return 1

        # we overshot the amount left (used too many coins)
        if amount_left < 0: return 0

        # we're out of denominations
        if current_index == len(denominations): return 0

        print "checking ways to make %i with %s" % (amount_left, denominations[current_index:])

        # choose a current coin
        current_coin = denominations[current_index]

        # see how many possibilities we can get
        # for each number of times to use current_coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(amount_left, denominations, current_index + 1)
            amount_left -= current_coin

        self.memo[memo_key] = num_possibilities
        return num_possibilities

class Test(unittest.TestCase):

    def test_cp(self):
        # self.assertEqual(3,CoinDenominator().change_possibilities_top_down(4, [1,2]))
        # self.assertEqual(3,CoinDenominator().change_possibilities_bottom_down(4, [1,2]))
        self.assertEqual(3,CoinDenominator().change_possibilities_bottom_down(5, [2,3,5]))

if __name__ == "__main__":
    unittest.main()
# coin_output(5, [1])
# CoinDenominator().change_possibilities_top_down(4, [1,2])
