import unittest

def find_unique_id(ids):
    id_count = {} 
    for each in ids:
        if each in id_count:
            del id_count[each]
        else:
            id_count[each] = 1
    
    for delivery_id, count in id_count.items():
        if count == 1: return delivery_id

class Test(unittest.TestCase):

    id_numbers = [3,5,6,8,23,3,5,23,8]
    def test_cp(self):
        self.assertEqual(6,find_unique_id(self.id_numbers))

if __name__ == "__main__":
    unittest.main()
