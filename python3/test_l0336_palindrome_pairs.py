import unittest

from l0336_palindrome_pairs import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted([[0, 1], [1, 0], [3, 2], [2, 4]]),
            sorted(Solution().palindromePairs(['abcd', 'dcba', 'lls', 's', 'sssll'])))
        self.assertEqual(
            sorted([[0, 1],[1, 0]]),
            sorted(Solution().palindromePairs(['bat', 'tab', 'cat'])))
