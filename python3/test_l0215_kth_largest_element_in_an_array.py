import unittest

from l0215_kth_largest_element_in_an_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(5, Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2))
        self.assertEqual(4, Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

