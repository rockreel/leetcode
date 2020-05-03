import unittest

from l0269_alien_dictinary import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('wertf', Solution().alienOrder(['wrt', 'wrf', 'er', 'ett', 'rftt']))
        self.assertEqual('zx', Solution().alienOrder(['z', 'x']))
        self.assertEqual('yxz', Solution().alienOrder(['zy', 'zx']))
        self.assertEqual('', Solution().alienOrder(['abc', 'bcd', 'qwert', 'ab']))
