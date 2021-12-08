import unittest

from l1346_check_If_n_and_Its_double_exist import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().checkIfExist([10, 2, 5, 3]))
        self.assertEqual(
            True, 
            Solution().checkIfExist([7, 1, 14, 11]))
        self.assertEqual(
            False, 
            Solution().checkIfExist([3, 1, 7, 11]))
        