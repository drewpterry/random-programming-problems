import unittest
# returns the times a meeting is happening
def merge_ranges(array):
    sorted_meetings = sorted(array)
    merged_list = [sorted_meetings[0]] 
    for current_meeting_start, current_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_list[-1]
        if last_merged_meeting_end >= current_meeting_start:
            merged_list[-1] = (last_merged_meeting_start, max(current_meeting_end, last_merged_meeting_end))
        else:
            merged_list.append((current_meeting_start, current_meeting_end))
    return merged_list 

class Test(unittest.TestCase):
    standard_array = [(0, 1), (3, 5), (5,7), (4, 8), (10, 12), (9, 10), (12,13)]

    def test_cp(self):
        self.assertEqual([(0, 1), (3, 8), (9, 13)],merge_ranges(self.standard_array))

if __name__ == "__main__":
    unittest.main()
