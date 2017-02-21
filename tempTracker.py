import unittest

class tempTracker:
    def __init__(self):
        self.max = None
        self.min = None
        self.mean = 0.0 
        self.number_of_values = 0
        self.sum = 0
        self.mode = None
        self.occurences = [0] * 111
        self.max_occurences = 0

    def insert(self, temp):
        self.all_temps.append(temp)
        self.max = max(temp, self.max)
        self.min= min(temp, self.min)
        self.set_mean(temp)
        self.set_mode(temp)
        return

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def set_mean(self, temp):
        self.number_of_values += 1
        self.sum += temp 
        self.mean = self.sum / self.number_of_values

    def get_mean(self):
        return self.mean

    def set_mode(self, temp):
        self.occurences[temp] += 1
        if self.occurences[temp] > self.max_occurences:
            self.max_occurences = temp
            self.mode = temp

    def get_mode(self):
        return self.mode

class Test(unittest.TestCase):

    def test_cp(self):

if __name__ == "__main__":
    unittest.main()
