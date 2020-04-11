import unittest

from l0078_subsets import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[1], []]),
            sorted(Solution().subsets([1])))
        self.assertEqual(
            sorted([[1], [2], [1, 2], []]),
            sorted(Solution().subsets([1, 2])))
        self.assertEqual(
            sorted([[3], [1], [2], [1, 2, 3], [1, 3], [2, 3], [1, 2], []]),
            sorted(Solution().subsets([1, 2, 3])))