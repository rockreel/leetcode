import unittest

from l0383_ransom_note import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):     
        self.assertEqual(False, Solution().canConstruct('a', 'b'))
        self.assertEqual(False, Solution().canConstruct('aa', 'ab'))
        self.assertEqual(True, Solution().canConstruct('aa', 'aab'))
