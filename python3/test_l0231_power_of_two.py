import unittest

from l0231_power_of_two import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(True, Solution().isPowerOfTwo(1))
        self.assertEqual(True, Solution().isPowerOfTwo(16))
        self.assertEqual(False, Solution().isPowerOfTwo(218))

