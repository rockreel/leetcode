# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self._nums = nums
        self._it = 0

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self._it < len(self._nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        next_ = self._nums[self._it]
        self._it += 1
        return next_

class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        else:
            self._next = None
        
    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        # if self._next is None and self._iterator.hasNext():
        #     self._next = self._iterator.next()
        return self._next

    def next(self):
        """
        :rtype: int
        """
        next_ = self._next
        self._next = None
        if self._iterator.hasNext():
            self._next = self._iterator.next()
        return next_
        
    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].