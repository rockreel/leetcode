import unittest

from l0072_edit_distance import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(3, Solution().minDistance('horse', 'ros'))
        self.assertEqual(5, Solution().minDistance('intention', 'execution'))