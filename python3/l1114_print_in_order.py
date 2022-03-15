import threading
from typing import Callable

class Foo:
    def __init__(self):
        self._first_called_lock = threading.Lock()
        self._second_called_lock = threading.Lock()
        self._first_called_lock.acquire()
        self._second_called_lock.acquire()
    
    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self._first_called_lock.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # printSecond() outputs "second". Do not change or remove this line.
        with self._first_called_lock:
            printSecond()
            self._second_called_lock.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        # printThird() outputs "third". Do not change or remove this line.
        with self._second_called_lock:
            printThird()