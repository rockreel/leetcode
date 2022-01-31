import unittest

from l1137_nth_tribonacci_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().tribonacci(4))
        self.assertEqual(1389537, Solution().tribonacci(25))
