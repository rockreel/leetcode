class MyCircularQueue:

    def __init__(self, k: int):
        self._queue = [0] * k
        self._head = -1
        self._tail = -1
        self._size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self._queue[0] = value
            self._head = 0
            self._tail = 0   
        else:
            tail = self._tail + 1 if self._tail + 1 <= self._size - 1 else 0
            self._queue[tail] = value
            self._tail = tail
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self._head == self._tail:
            self._head = -1
            self._tail = -1
        else:
            head = self._head + 1 if self._head + 1 <= self._size - 1 else 0
            self._head = head
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._queue[self._head]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._queue[self._tail]

    def isEmpty(self) -> bool:
        return self._head == -1 and self._tail == -1

    def isFull(self) -> bool:
        if self._tail == self._size - 1:
            return self._head == 0
        else:
            return self._head == self._tail + 1
        
# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()