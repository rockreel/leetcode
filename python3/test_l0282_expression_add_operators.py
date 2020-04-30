import unittest

from l0282_expression_add_operators import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(sorted(['1+2+3', '1*2*3']), sorted(Solution().addOperators('123', 6)))
        self.assertEqual(sorted(['2*3+2', '2+3*2']), sorted(Solution().addOperators('232', 8)))
        self.assertEqual(sorted(['1*0+5', '10-5']), sorted(Solution().addOperators('105', 5)))
        self.assertEqual(sorted(['0+0', '0-0', '0*0']), sorted(Solution().addOperators('00', 0)))
        # self.assertEqual([], Solution().addOperators('3456237490', 9191))
