class Solution:
    def tribonacci(self, n: int) -> int:
        tr = [0] * max(3, n+1)
        tr[1] = 1
        tr[2] = 1
        for i in range(3, n+1):
            tr[i] = tr[i-1] + tr[i-2] + tr[i-3]
        return tr[n]