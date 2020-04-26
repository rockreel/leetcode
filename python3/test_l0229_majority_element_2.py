import unittest

from l0229_majority_element_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([3], Solution().majorityElement([3, 2, 3]))
        self.assertEqual([1, 2], Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
        self.assertEqual([1, 2], Solution().majorityElement([1, 2]))
