from typing import Callable
import threading

class FizzBuzz:
    def __init__(self, n: int):
        self.n = n
        self.i = 1
        self.lock_number = threading.Semaphore(1)
        self.lock_fizz = threading.Semaphore(0)
        self.lock_buzz = threading.Semaphore(0)
        self.lock_fizzbuzz = threading.Semaphore(0)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 != 0:
                self.lock_fizz.acquire()
                printFizz()
                self.lock_number.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 != 0 and i % 5 == 0:
                self.lock_buzz.acquire()
                printBuzz()
                self.lock_number.release()

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.lock_fizzbuzz.acquire()
                printFizzBuzz()
                self.lock_number.release()

    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n+1):
            self.lock_number.acquire()
            if i % 3 == 0 and i % 5 != 0:
                self.lock_fizz.release()
            elif i % 3 != 0 and i % 5 == 0:
                self.lock_buzz.release()
            elif i % 3 == 0 and i % 5 == 0:
                self.lock_fizzbuzz.release()
            else:
                printNumber(i)
                self.lock_number.release()