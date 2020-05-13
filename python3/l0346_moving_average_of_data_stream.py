class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self._size = size
        self._nums = []
        self._sum = 0
        

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        if len(self._nums) == self._size:
            self._sum -= self._nums.pop(0)
        self._nums.append(val)
        self._sum += val
        return self._sum / len(self._nums)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
