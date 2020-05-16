import unittest

from l0346_moving_average_of_data_stream import MovingAverage

class Test(unittest.TestCase):
    
    def test_solution(self):
        ma = MovingAverage(3)
        self.assertTrue(abs(ma.next(1) - 1.0) < 0.0001)
        self.assertTrue(abs(ma.next(10) - 5.5) < 0.0001)
        self.assertTrue(abs(ma.next(3) - 4.6667) < 0.0001)
        self.assertTrue(abs(ma.next(5) - 6.0) < 0.0001)