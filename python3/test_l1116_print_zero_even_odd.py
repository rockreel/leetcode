import unittest
import threading

from l1116_print_zero_even_odd import ZeroEvenOdd

class Test(unittest.TestCase):
    
    def test_solution(self):
        zeo = ZeroEvenOdd(3)

        t1 = threading.Thread(target=lambda: zeo.zero(lambda x: print(x)))
        t2 = threading.Thread(target=lambda: zeo.even(lambda x: print(x)))
        t3 = threading.Thread(target=lambda: zeo.odd(lambda x: print(x)))
    
        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
        
