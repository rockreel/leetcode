import unittest

from l0018_4_sum import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
          set([(-1, 0, 0, 1), (-2, -1, 1, 2), (-2, 0, 0, 2)]),
          set([(r[0], r[1], r[2], r[3]) for r in Solution().fourSum([1, 0, -1, 0, -2, 2], 0)]))

