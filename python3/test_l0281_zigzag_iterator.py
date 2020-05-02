import unittest

from l0281_zigzag_iterator import ZigzagIterator

class Test(unittest.TestCase):
    
    def test_solution(self):
        it = ZigzagIterator([1, 2], [3, 4, 5, 6])
        self.assertEqual(1, it.next())
        self.assertEqual(3, it.next())
        self.assertEqual(2, it.next())
        self.assertEqual(4, it.next())
        self.assertEqual(5, it.next())
        self.assertEqual(6, it.next())
        self.assertEqual(False, it.hasNext())

        it = ZigzagIterator([1, 1, 1, 1], [3, 4, 5, 6])
        self.assertEqual(1, it.next())
        self.assertEqual(3, it.next())
        self.assertEqual(1, it.next())
        self.assertEqual(4, it.next())
        self.assertEqual(1, it.next())
        self.assertEqual(5, it.next())
        self.assertEqual(1, it.next())
        self.assertEqual(6, it.next())
        self.assertEqual(False, it.hasNext())