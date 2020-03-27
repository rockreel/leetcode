import unittest

from l0028_implement_strstr import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(2, Solution().strStr('hello', 'll'))
        self.assertEqual(-1, Solution().strStr('aaaaa', 'bba'))