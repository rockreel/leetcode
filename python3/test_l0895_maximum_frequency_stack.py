import unittest

from l0895_maximum_frequency_stack import FreqStack

class Test(unittest.TestCase):
    
    def test_solution(self):
        fs = FreqStack()
        fs.push(5)
        fs.push(7)
        fs.push(5)
        fs.push(7)
        fs.push(4)
        fs.push(5)
        self.assertEqual(5, fs.pop())
        self.assertEqual(7, fs.pop())
        self.assertEqual(5, fs.pop())
        self.assertEqual(4, fs.pop())
