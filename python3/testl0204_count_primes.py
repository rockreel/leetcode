import unittest

from l0204_count_primes import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(4, Solution().countPrimes(10))

