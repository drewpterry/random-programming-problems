import unittest

# sort values in 0(n) time, highest score is 100
def sort_scores(scores):
    highest_possible_score = 100
    score_counts = [0] * (highest_possible_score+1)
    sorted_scores = list() 
    for value in scores:
        score_counts[value] = score_counts[value] + 1

    for i, each in reversed(list(enumerate(score_counts))):
        for score in range(score_counts[i]):
            sorted_scores.append(i)

    return sorted_scores

class Test(unittest.TestCase):

    def test_sort_scores(self):
        scores = [4, 99, 22]
        scores2 = [3, 3, 5]
        self.assertEqual([99, 22, 4], sort_scores(scores))
        self.assertEqual([5, 3 ,3], sort_scores(scores2))

if __name__ == "__main__":
    unittest.main()
