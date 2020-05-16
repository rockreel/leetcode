import unittest

from l0344_reverse_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        l = ['h', 'e', 'l', 'l', 'o']
        Solution().reverseString(l)
        self.assertEqual(['o', 'l', 'l', 'e', 'h'], l)

        l = ['H', 'a', 'n', 'n', 'a', 'h']
        Solution().reverseString(l)
        self.assertEqual(['h', 'a', 'n', 'n', 'a', 'H'], l)