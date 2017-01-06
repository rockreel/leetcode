class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        
        nums = [str(i+1) for i in range(n)]
        result = []
        k -= 1  # Shit k to be 0 based.
        while nums:
            block_size = math.factorial(len(nums)-1)
            result.append(nums.pop(k/block_size))
            k =  k % block_size
            
        return ''.join(result)

