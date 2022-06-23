import unittest

from l0496_next_greater_element_1 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [-1,3,-1], 
            Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
        self.assertEqual(
            [3,-1], 
            Solution().nextGreaterElement([2,4], [1,2,3,4]))
