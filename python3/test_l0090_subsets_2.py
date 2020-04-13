import unittest

from l0090_subsets_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[2], [1], [1, 2, 2], [2, 2], [1, 2], []]),
            sorted(Solution().subsetsWithDup([1, 2, 2])))