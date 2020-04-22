import unittest

from l0157_read_n_characters_give_read_4 import Reader
from l0157_read_n_characters_give_read_4 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        buf = []
        read = Solution()

        Reader.input = '1234567'
        Reader.pos = 0
        self.assertEqual(6, read.read(buf, 6))
        self.assertEqual(list('123456'), buf[:6])

        Reader.pos = 0
        self.assertEqual(5, read.read(buf, 5))
        self.assertEqual(list('12345'), buf[:5])

        Reader.pos = 0
        self.assertEqual(7, read.read(buf, 10))
        self.assertEqual(list('1234567'), buf[:7])

