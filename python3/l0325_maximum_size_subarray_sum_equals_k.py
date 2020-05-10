class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        # Sum from nums[i] to nums[j] is sums[j+1] - sums[i].
        sums = [0]
        sum_to_idx = dict()
        for i, n in enumerate(nums):
            sums.append(sums[-1] + n)
            sum_to_idx[sums[-1]] = i + 1
        max_len = 0
        for i, s0 in enumerate(sums):
            s1 = k + s0
            if s1 in sum_to_idx:
                len = sum_to_idx[s1] - i
                max_len = max(max_len, len)
        return max_len
