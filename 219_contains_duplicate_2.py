class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        num_index_map = {}
        for i, n in enumerate(nums):
            if n not in num_index_map:
                num_index_map[n] = i
            else:
                if i - num_index_map[n] <= k:
                    return True
                else:
                    num_index_map[n] = i
        return False

