import threading
from typing import Callable

class FooBar:
    def __init__(self, n):
        self.n = n
        self.count_foo = 0
        self.count_bar = 0
        self.condition = threading.Condition()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.count_bar == self.count_foo)
                # printFoo() outputs "foo". Do not change or remove this line.
                printFoo()
                self.count_foo += 1
                self.condition.notify(1)


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with self.condition:
                self.condition.wait_for(lambda: self.count_foo > self.count_bar)
                # printBar() outputs "bar". Do not change or remove this line.
                printBar()
                self.count_bar += 1
                self.condition.notify(1)