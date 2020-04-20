import unittest

from l0155_min_stack import MinStack

class Test(unittest.TestCase):
    
    def test_solution(self):
        minStack = MinStack()
        minStack.push(-2)
        minStack.push(0)
        minStack.push(-3)
        self.assertEqual(-3, minStack.getMin())
        minStack.pop()
        minStack.top()
        self.assertEqual(-2, minStack.getMin())