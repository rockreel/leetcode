import unittest

from l0284_peeking_iterator import Iterator
from l0284_peeking_iterator import PeekingIterator

class Test(unittest.TestCase):
    
    def test_solution(self):
        it = Iterator([1, 2, 3])
        pit = PeekingIterator(it)
        self.assertEqual(1, pit.next())
        self.assertEqual(2, pit.peek())
        self.assertEqual(2, pit.next())
        self.assertEqual(3, pit.next())
        self.assertEqual(False, pit.hasNext())