import unittest

from l0622_design_circular_queue import MyCircularQueue

class Test(unittest.TestCase):
    
    def test_solution(self):
        queue = MyCircularQueue(3)
        self.assertTrue(queue.enQueue(1))
        self.assertTrue(queue.enQueue(2))
        self.assertTrue(queue.enQueue(3))
        self.assertFalse(queue.enQueue(4))
        self.assertEqual(3, queue.Rear())
        self.assertTrue(queue.isFull())
        self.assertTrue(queue.deQueue())
        self.assertTrue(queue.enQueue(4))
        self.assertEqual(4, queue.Rear())