import unittest

from l0278_first_bad_version import Solution
import l0278_first_bad_version 

class Test(unittest.TestCase):
    
    def test_solution(self):
        l0278_first_bad_version.versions = [False, False, False, False, True, True, True]
        self.assertEqual(4, Solution().firstBadVersion(5))
