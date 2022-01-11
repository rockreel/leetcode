import unittest

from l0394_decode_string import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('aaabcbc', Solution().decodeString('3[a]2[bc]'))
        self.assertEqual('accaccacc', Solution().decodeString('3[a2[c]]'))
        self.assertEqual('abcabccdcdcdef', Solution().decodeString('2[abc]3[cd]ef'))
