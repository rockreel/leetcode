class NumArray:

    def __init__(self, nums: List[int]):
        self._n = n = len(nums)
        self._tree = [0] * (2 * n)
        for i in range(n):
            self._tree[n+i] = nums[i]
        for i in range(n-1, 0, -1):
            self._tree[i] = self._tree[2*i] + self._tree[2*i+1]

        

    def update(self, i: int, val: int) -> None:
        diff = val - self._tree[self._n+i]
        j = self._n + i
        while j > 0:
            self._tree[j] += diff
            if j % 2 == 0:
                j = j // 2
            else:
                j = (j - 1) // 2
        

    def sumRange(self, i: int, j: int) -> int:
        i = self._n + i
        j = self._n + j
        sum_ = 0
        while i <= j:
            if i % 2 == 1:
                # Lower bound right child, include itself.
                sum_ += self._tree[i]
                i += 1
                
            if j  % 2 == 0:
                # Upper bound left child, include itself.
                sum_ += self._tree[j]
                j -= 1
                
            i = i // 2
            j = (j - 1) // 2
        return sum_
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
