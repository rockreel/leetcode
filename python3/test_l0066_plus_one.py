import unittest

from l0066_plus_one import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual([1, 2, 4], Solution().plusOne([1, 2, 3]))
        self.assertEqual([4, 3, 2, 2], Solution().plusOne([4, 3, 2, 1]))
        self.assertEqual([1, 0, 0, 0], Solution().plusOne([9, 9, 9]))
