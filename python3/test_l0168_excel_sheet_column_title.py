import unittest

from l0168_excel_sheet_column_title import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual('A', Solution().convertToTitle(1))
        self.assertEqual('Z', Solution().convertToTitle(26))
        self.assertEqual('AB', Solution().convertToTitle(28))
        self.assertEqual('ZY', Solution().convertToTitle(701))