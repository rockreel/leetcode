class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 1 bits in xor are different bits in two single numbers.
        # Find the lowest one, use it to split original list
        # and apply xor trick to find single numbers respectively.
        xor = reduce(lambda x, y: x^y, nums)
        lowest_bit = 1
        while lowest_bit & xor == 0:
            lowest_bit <<= 1
        r1, r2 = 0, 0
        for n in nums:
            if n & lowest_bit > 0:
                r1 ^= n
            else:
                r2 ^= n
        return [r1, r2]

