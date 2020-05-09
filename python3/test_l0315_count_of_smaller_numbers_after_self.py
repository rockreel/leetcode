import unittest

from l0315_count_of_smaller_numbers_after_self import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([2, 1, 1, 0], Solution().countSmaller([5, 2, 6, 1]))
