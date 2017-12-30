import unittest

def reverse_words(s):
    words = s.split(' ') 
    first_place = 0
    last_place = len(words) - 1

    while first_place < last_place:
        words[first_place], words[last_place] = words[last_place], words[first_place]
        first_place += 1
        last_place -= 1
        
    return ' '.join(words)
    

class Test(unittest.TestCase):

    def test_reverses_words(self):
        self.assertEqual('this is a message', reverse_words('message a is this'))
        self.assertEqual('this is a message a', reverse_words('a message a is this'))

if __name__ == "__main__":
    unittest.main()
