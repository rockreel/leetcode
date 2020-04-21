import unittest

from l0187_repeated_dna_sequences import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        self.assertEqual(
            sorted(['AAAAACCCCC', 'CCCCCAAAAA']),
            sorted(Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')))