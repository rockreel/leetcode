import unittest

from l0547_number_of_provinces import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            2, 
            Solution().findCircleNum([[1, 1, 0], [1, 1, 0],[0, 0, 1]]))
        self.assertEqual(
            3,
            Solution().findCircleNum([[1, 0, 0], [0, 1, 0],[0, 0, 1]]))


