import unittest

from l0158_read_n_characters_give_read_4_2 import Reader
from l0158_read_n_characters_give_read_4_2 import Solution

class Test(unittest.TestCase):
    
    def test_solution(self):
        buf = []
        Reader.input = 'filetestbuffer'
        Reader.pos = 0
        read = Solution()
        self.assertEqual(6, read.read(buf, 6))
        self.assertEqual(list('filete'), buf[:6])
        self.assertEqual(5, read.read(buf, 5))
        self.assertEqual(list('stbuf'), buf[:5])
        self.assertEqual(3, read.read(buf, 4))
        self.assertEqual(list('fer'), buf[:3])
        self.assertEqual(0, read.read(buf, 3))
        self.assertEqual(0, read.read(buf, 2))
        self.assertEqual(0, read.read(buf, 1))
        self.assertEqual(0, read.read(buf, 10))

        Reader.input = 'abcdef'
        Reader.pos = 0
        read = Solution()
        self.assertEqual(1, read.read(buf, 1))
        self.assertEqual(list('a'), buf[:1])
        self.assertEqual(5, read.read(buf, 5))
        self.assertEqual(list('bcdef'), buf[:5])

        Reader.input = 'ab'
        Reader.pos = 0
        read = Solution()
        self.assertEqual(1, read.read(buf, 1))
        self.assertEqual(list('a'), buf[:1])
        self.assertEqual(1, read.read(buf, 2))
        self.assertEqual(list('b'), buf[:1])