class NumArray:

    def __init__(self, nums: List[int]):
        self._sums = [0]

        for n in nums:
            self._sums.append(
                self._sums[-1] + n)


    def sumRange(self, i: int, j: int) -> int:
        return self._sums[j+1] - self._sums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
