class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessar
        self._v1 = v1
        self._v2 = v2
        self._i1 = 0
        self._i2 = 0
        self._s = 1
        if not self.hasNext():
            self._s = -self._s 

    """
    @return: An integer
    """
    def next(self):
        # write your code here
        if self._s == 1: 
            v = self._v1[self._i1]
            self._i1 += 1
            self._s = -1 
        else:
            v = self._v2[self._i2]
            self._i2 += 1
            self._s = 1
        if not self.hasNext(): 
            self._s = -self._s 
        return v 


    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code her
        if self._s == 1:
            return self._i1 < len(self._v1)
        else:
            return self._i2 < len(self._v2)
        


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result
