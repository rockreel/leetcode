import unittest

from l0318_maximum_product_of_word_lengths import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(16, Solution().maxProduct(['abcw', 'baz', 'foo', 'bar', 'xtfn', 'abcdef']))
        self.assertEqual(4, Solution().maxProduct(['a', 'ab', 'abc', 'd', 'cd', 'bcd', 'abcd']))
        self.assertEqual(0, Solution().maxProduct(['a', 'aa', 'aaa', 'aaaa']))
