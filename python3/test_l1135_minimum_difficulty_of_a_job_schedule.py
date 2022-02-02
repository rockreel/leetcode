import unittest

from l1135_minimum_difficulty_of_a_job_schedule import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            7, 
            Solution().minDifficulty([6, 5, 4, 3, 2, 1], 2))
        self.assertEqual(
            -1, 
            Solution().minDifficulty([9, 9, 9], 4))
        self.assertEqual(
            3, 
            Solution().minDifficulty([1, 1, 1], 3))
