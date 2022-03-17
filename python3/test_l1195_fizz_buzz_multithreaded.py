import unittest
import threading

from l1195_fizz_buzz_multithreaded import FizzBuzz

class Test(unittest.TestCase):
    
    def test_solution(self):
        fb = FizzBuzz(5)

        t1 = threading.Thread(target=lambda: fb.fizz(lambda: print('fizz')))
        t2 = threading.Thread(target=lambda: fb.buzz(lambda: print('buzz')))
        t3 = threading.Thread(target=lambda: fb.fizzbuzz(lambda: print('fizzbuzz')))
        t4 = threading.Thread(target=lambda: fb.number(lambda x: print(x)))

        t1.start()
        t2.start()
        t3.start()
        t4.start()

        t1.join()
        t2.join()
        t3.join()
        t4.join()

