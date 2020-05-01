import unittest

from l0271_encode_and_decode_strings import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            ['lint', 'code', 'love', 'you'],
            Solution().decode(Solution().encode(['lint', 'code', 'love', 'you'])))
        self.assertEqual(
            ['we', 'say', ':', 'yes'],
            Solution().decode(Solution().encode(['we', 'say', ':', 'yes'])))
        self.assertEqual(
            ['we:', ';say:;', ':;', ';;:yes::;'],
            Solution().decode(Solution().encode(['we:', ';say:;', ':;', ';;:yes::;'])))
