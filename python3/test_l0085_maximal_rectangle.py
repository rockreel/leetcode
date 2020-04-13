import unittest

from l0085_maximal_rectangle import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            6,
            Solution().maximalRectangle(
                [
                    ['1', '0', '1', '0', '0'],
                    ['1', '0', '1', '1', '1'],
                    ['1', '1', '1', '1', '1'],
                    ['1', '0', '0', '1', '0']
                ]   
            ))
        self.assertEqual(
            1,
            Solution().maximalRectangle(
                [
                    ['0', '1'],
                    ['1', '0']
                ]   
            ))