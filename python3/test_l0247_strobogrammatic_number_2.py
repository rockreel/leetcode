import unittest

from l0247_strobogrammatic_number_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(['11', '69', '88', '96'], sorted(Solution().findStrobogrammatic(2)))
        self.assertEqual(['0', '1', '8'], sorted(Solution().findStrobogrammatic(1)))
