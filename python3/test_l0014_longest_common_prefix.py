import unittest

from l0014_longest_common_prefix import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('fl', Solution().longestCommonPrefix(['flower', 'flow', 'flight']))
        self.assertEqual('', Solution().longestCommonPrefix(['dog', 'racecar', 'car']))