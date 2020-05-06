import unittest

from l0305_number_of_islands_2 import Point
from l0305_number_of_islands_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 1, 2, 2], Solution().numIslands2(4, 5, [Point(1, 1), Point(0, 1), Point(3, 3), Point(3, 4)]))
        self.assertEqual([1, 1, 2, 2], Solution().numIslands2(3, 3, [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 1)]))
        self.assertEqual([1, 1, 2, 2], Solution().numIslands2(3, 3, [Point(0, 0), Point(0, 1), Point(2, 2), Point(2, 2)]))
        self.assertEqual(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 11, 12, 12, 12, 12, 12, 13, 13, 14, 15, 16, 17,
             18, 18, 18, 19, 19, 18, 17, 16, 16, 16, 16, 16, 16, 17, 17, 16, 16, 17, 18, 18, 18, 17, 17, 17],
            Solution().numIslands2(8, 14, [
                Point(0,9), Point(5,4), Point(0,12), Point(6,9), Point(6,5), Point(0,4),
                Point(4,11), Point(0,0), Point(3,5), Point(6,7), Point(3,12), Point(0,5),
                Point(6,13), Point(7,5), Point(3,6), Point(4,4), Point(0,8), Point(3,1),
                Point(4,6), Point(6,1), Point(5,12), Point(3,8), Point(7,0), Point(2,9),
                Point(1,4), Point(3,0), Point(1,13), Point(2,13), Point(6,0), Point(6,4),
                Point(0,13), Point(0,3), Point(7,4), Point(1,8), Point(5,5), Point(5,7),
                Point(5,10), Point(5,3), Point(6,10), Point(6,2), Point(3,10), Point(2,7),
                Point(1,12), Point(5,0), Point(4,5), Point(7,13), Point(3,2)]))