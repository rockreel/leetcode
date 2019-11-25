class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        import sys
        def findKthElement(nums1, nums2, k):
            if not nums1:
                return nums2[k-1]
            if not nums2:
                return nums1[k-1]
            if k == 1:
                return min(nums1[0], nums2[0])
            
            m1 = nums1[k/2-1] if k/2 - 1 < len(nums1) else sys.maxint
            m2 = nums2[k/2-1] if k/2 - 1 < len(nums2) else sys.maxint
            if m1 < m2:
                return findKthElement(nums1[k/2:], nums2, k - k/2 )
            else:
                return findKthElement(nums1, nums2[k/2:], k - k/2 )

        k = len(nums1) + len(nums2)
        if k % 2 == 0:
            return (findKthElement(nums1, nums2, k/2) + findKthElement(nums1, nums2, k/2+1)) / 2.0
        else:
            return findKthElement(nums1, nums2, k/2+1)