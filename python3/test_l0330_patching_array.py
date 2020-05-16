import unittest

from l0330_patching_array import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().minPatches([1, 3], 6))
        self.assertEqual(2, Solution().minPatches([1, 5, 10], 20))
        self.assertEqual(0, Solution().minPatches([1, 2, 2], 5))
