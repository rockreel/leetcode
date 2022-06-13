import unittest

from l0844_backspace_string_compare import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            True, 
            Solution().backspaceCompare('ab#c', 'ad#c'))
        self.assertEqual(
            True, 
            Solution().backspaceCompare('ab##', 'c#d#'))
        self.assertEqual(
            False, 
            Solution().backspaceCompare('a#c', 'b'))

