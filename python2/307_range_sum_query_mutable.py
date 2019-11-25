class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self._nums = [0] * len(nums)
        self._bit = [0] * (len(nums)+1)
        for i, n in enumerate(nums):
            self.update(i, n)
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self._nums[i]
        self._nums[i] += diff
        i = i + 1
        while i < len(self._bit):
            self._bit[i] += diff
            i = i + (i&-i)
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sumTo(j) - self.sumTo(i-1)

    def sumTo(self, i):
        # Sum from nums[0] to nums[i].
        sum = 0
        i = i + 1
        while i > 0:
            sum += self._bit[i]
            i = i - (i&-i)
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

