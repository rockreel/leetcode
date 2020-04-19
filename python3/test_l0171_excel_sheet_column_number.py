import unittest

from l0171_excel_sheet_column_number import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(1, Solution().titleToNumber('A'))
        self.assertEqual(26, Solution().titleToNumber('Z'))
        self.assertEqual(28, Solution().titleToNumber('AB'))
        self.assertEqual(701, Solution().titleToNumber('ZY'))