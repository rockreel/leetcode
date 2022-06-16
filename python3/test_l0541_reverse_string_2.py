import unittest

from l0541_reverse_string_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('bacdfeg', Solution().reverseStr('abcdefg', 2))
        self.assertEqual('bacd', Solution().reverseStr('abcd', 2))
