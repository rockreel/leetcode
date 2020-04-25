import unittest

from l0232_implement_queue_using_stacks import MyQueue

class Test(unittest.TestCase):
    
    def test_solution(self):
        queue = MyQueue()
        queue.push(1)
        queue.push(2)
        self.assertEqual(1, queue.peek())
        self.assertEqual(1, queue.pop())
        self.assertEqual(False, queue.empty())