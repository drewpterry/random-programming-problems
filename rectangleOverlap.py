import unittest
#return the overlapping the rectangle formed by the intersection of two rectangles
class Rectangles:
    def __overlap(self, point1, length1, point2, length2):
        highest_startpoint = max(point1, point2)
        lowest_endpoint = min(point1+length1, point2+length2)
        if highest_startpoint >= lowest_endpoint:
            return (None, None) 

        return (highest_startpoint, lowest_endpoint - highest_startpoint)

    def overlappingRectangle(self, first_rectangle, second_rectangle):
        x_left, x_width = self.__overlap(first_rectangle['left_x'],first_rectangle['width'], second_rectangle['left_x'], second_rectangle['width'])
        y_bottom, y_height = self.__overlap(first_rectangle['bottom_y'],first_rectangle['height'], second_rectangle['bottom_y'], second_rectangle['height'])
        if not x_width or not y_height:
            return None

        rectangle = {}
        rectangle['left_x'] = x_left
        rectangle['width'] = x_width 
        rectangle['bottom_y'] = y_bottom 
        rectangle['height'] = y_height
        return rectangle 

class Test(unittest.TestCase):
    rectangle_one = {
            'left_x' : 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2
            }
    rectangle_two = {
            'left_x' : 2,
            'bottom_y': 0,
            'width': 2,
            'height': 4
            }

    result_rectangle = {
            'left_x' : 2,
            'bottom_y': 1,
            'width': 1,
            'height': 2
            }

    def test_cp(self):
        self.assertEqual(self.result_rectangle, Rectangles().overlappingRectangle(self.rectangle_one, self.rectangle_two))

if __name__ == "__main__":
    unittest.main()
