import threading
from typing import Callable

class H2O:
    def __init__(self):
        self.sema_o = threading.Semaphore(1)
        self.sema_h = threading.Semaphore(2)
        self.barrier = threading.Barrier(3)

    def hydrogen(self, releaseHydrogen: 'Callable[[], None]') -> None:
        self.sema_h.acquire()
        self.barrier.wait()
        # releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen()
        self.sema_h.release()

    def oxygen(self, releaseOxygen: 'Callable[[], None]') -> None:
        self.sema_o.acquire()
        self.barrier.wait()
        # releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen()
        self.sema_o.release()