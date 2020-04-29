class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n0 = 0
        for n in nums:
            n0 ^= n
        # Find one bit can divide array into two.
        mask = 1
        while mask & n0 == 0:
            mask <<= 1
        
        n1, n2 = 0, 0
        for n in nums:
            if mask & n == 0:
                n1 ^= n
            else:
                n2 ^= n
        return [n1, n2]
