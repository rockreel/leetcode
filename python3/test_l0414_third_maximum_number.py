import unittest

from l0414_third_maximum_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            1, 
            Solution().thirdMax([3, 2, 1]))
        self.assertEqual(
            2, 
            Solution().thirdMax([1, 2]))
        self.assertEqual(
            1, 
            Solution().thirdMax([2, 2, 3, 1]))
        