import unittest

from l0205_isomorphic_strings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isIsomorphic('egg', 'add'))
        self.assertEqual(False, Solution().isIsomorphic('foo', 'bar'))
        self.assertEqual(True, Solution().isIsomorphic('paper', 'title'))

