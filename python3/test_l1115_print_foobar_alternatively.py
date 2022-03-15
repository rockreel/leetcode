import unittest
import threading

from l1115_print_foobar_alternatively import FooBar

class Test(unittest.TestCase):
    
    def test_solution(self):
        foobar = FooBar(3)

        t1 = threading.Thread(target=lambda: foobar.foo(lambda: print('foo')))
        t2 = threading.Thread(target=lambda: foobar.bar(lambda: print('bar')))
    
        t1.start()
        t2.start()

        t1.join()
        t2.join()
        
