import unittest

from l0067_add_binary import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        # self.assertEqual('100', Solution().addBinary('11', '1'))
        self.assertEqual('10101', Solution().addBinary('1010', '1011'))