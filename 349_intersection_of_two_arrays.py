class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num_set = set(nums2)
        return [n for n in set(nums1) if n in num_set]

