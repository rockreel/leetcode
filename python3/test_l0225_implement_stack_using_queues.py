import unittest

from l0225_implement_stack_using_queues import MyStack

class Test(unittest.TestCase):
    
    def test_solution(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(2, stack.top())
        self.assertEqual(2, stack.pop())
        self.assertEqual(False, stack.empty())