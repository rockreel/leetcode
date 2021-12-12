class MyLinkedList:

    class Node:
        def __init__(self, val, next=None):
            self.val = val
            self.next = next

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index >= self.size or index < 0:
            return -1
        i = 0
        p = self.head
        while i < index and p:
            p = p.next
            i += 1
        return p.val if p else None
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        dummy = MyLinkedList.Node(0, self.head)
        p = dummy
        i = 0
        while i < index:
            p = p.next
            i += 1
        node = MyLinkedList.Node(val, p.next)
        p.next = node
        self.size += 1
        self.head = dummy.next
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size or index < 0:
            return
        dummy = MyLinkedList.Node(0, self.head)
        p = dummy
        i = 0
        while i < index:
            p = p.next
            i += 1
        p.next = p.next.next
        self.size -= 1
        self.head = dummy.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)