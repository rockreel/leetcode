import unittest

from l0239_sliding_window_maximum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([3, 3, 5, 5, 6, 7] , Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))