import unittest
def reverse_string(s):
    string_list = list(s) 
    length = len(string_list)
    for i in range(0,length):
        if i <= length/2 - 1:
            string_list[i], string_list[length-1-i] = string_list[length-1-i], string_list[i]
        
    return ''.join(string_list)
    

class Test(unittest.TestCase):

    def test_reverses_string(self):
        self.assertEqual('olleh', reverse_string('hello'))
        self.assertEqual('ollehs', reverse_string('shello'))

if __name__ == "__main__":
    unittest.main()
