import unittest

from l0161_one_edit_distance import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isOneEditDistance('aDb', 'adb'))
        self.assertEqual(True, Solution().isOneEditDistance('ab', 'adb'))
        self.assertEqual(True, Solution().isOneEditDistance('aDb', 'ab'))
        self.assertEqual(False, Solution().isOneEditDistance('ab', 'ab'))
        self.assertEqual(False, Solution().isOneEditDistance('ab', 'abcd'))
