class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        result = []
        for n in counter1:
            if n in counter2:
                result.extend([n]*min(counter1[n], counter2[n]))
        return result

