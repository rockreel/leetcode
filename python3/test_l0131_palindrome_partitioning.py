import unittest

from l0131_palindrome_partitioning import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([
                ['aa', 'b'],
                ['a', 'a', 'b']
            ]), 
            sorted(Solution().partition('aab')))
        self.assertEqual(
            sorted([
                ['b', 'b'],
                ['bb']
            ]), 
            sorted(Solution().partition('bb')))
