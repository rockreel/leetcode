import unittest

from l0455_assign_cookcies import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().findContentChildren([1,2,3], [1,1]))
        self.assertEqual(2, Solution().findContentChildren([1,2], [1,2,3]))