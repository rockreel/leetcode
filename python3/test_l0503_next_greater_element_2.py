import unittest

from l0503_next_greater_element_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [2,-1,2], 
            Solution().nextGreaterElements([1,2,1]))
        self.assertEqual(
            [2,3,4,-1,4], 
            Solution().nextGreaterElements([1,2,3,4,3]))
