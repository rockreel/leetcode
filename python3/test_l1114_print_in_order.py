import unittest
import threading

from l1114_print_in_order import Foo

class Test(unittest.TestCase):
    
    def test_solution(self):
        def printFirst():
            print('first')

        def printSecond():
            print('second')
        
        def printThird():
            print('third')

        foo = Foo()

        t1 = threading.Thread(target=lambda: foo.third(printThird))
        t2 = threading.Thread(target=lambda: foo.second(printSecond))
        t3 = threading.Thread(target=lambda: foo.first(printFirst))

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()
        
