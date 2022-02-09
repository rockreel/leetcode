import unittest

from l1337_the_k_weakest_rows_in_a_matrix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            [2, 0, 3], 
            Solution().kWeakestRows([[1,1,0,0,0], [1,1,1,1,0], [1,0,0,0,0], [1,1,0,0,0], [1,1,1,1,1]], 3))
        self.assertEqual(
            [0, 2], 
            Solution().kWeakestRows([[1,0,0,0], [1,1,1,1], [1,0,0,0], [1,0,0,0]], 2))

        