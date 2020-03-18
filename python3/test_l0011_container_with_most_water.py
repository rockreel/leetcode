import unittest

from l0011_container_with_most_water import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(49, Solution().maxArea([1,8,6,2,5,4,8,3,7]))
