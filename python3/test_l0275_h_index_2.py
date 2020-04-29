import unittest

from l0274_h_index import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().hIndex([0, 1, 3, 5, 6]))
