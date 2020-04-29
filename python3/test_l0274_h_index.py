import unittest

from l0274_h_index import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().hIndex([3, 0, 6, 1, 5]))
