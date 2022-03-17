import threading
from typing import Callable

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.i = 0
        self.lock_even = threading.Lock()
        self.lock_odd = threading.Lock()
        self.lock_zero = threading.Lock()
        self.lock_odd.acquire()
        self.lock_even.acquire()
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n):
            self.lock_zero.acquire()
            printNumber(0)
            self.i += 1
            if self.i % 2 == 1: 
                self.lock_odd.release()
            else:
                self.lock_even.release()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n // 2):
            self.lock_even.acquire()
            printNumber(self.i)
            self.lock_zero.release()
        
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range((self.n + 1) // 2):
            self.lock_odd.acquire()
            printNumber(self.i)
            self.lock_zero.release()