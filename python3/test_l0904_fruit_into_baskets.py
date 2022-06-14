import unittest

from l0904_fruit_into_baskets import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            3,
            Solution().totalFruit([1,2,1]))
        self.assertEqual(
            3,
            Solution().totalFruit([0,1,2,2]))
        self.assertEqual(
            4,
            Solution().totalFruit([1,2,3,2,2]))