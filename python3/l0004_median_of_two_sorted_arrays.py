from typing import List

# Recursion.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(nums1, nums2, k):
            if not nums1:
                return nums2[k]
            if not nums2:
                return nums1[k]
            if k == 0:
                return min(nums1[0], nums2[0])
            
            m = (k - 1) // 2
            m1 = nums1[m] if m < len(nums1) else float('inf')
            m2 = nums2[m] if m < len(nums2) else float('inf')
            
            if m1 < m2:
                return findKthElement(nums1[m+1:], nums2, k - m - 1)
            else:
                return findKthElement(nums1, nums2[m+1:], k - m - 1)
            
        n1 = len(nums1)
        n2 = len(nums2)
        if (n1 + n2) % 2 == 0:
            return (findKthElement(nums1, nums2, (n1 + n2) // 2 - 1) + findKthElement(nums1, nums2, (n1 + n2) // 2)) / 2
        else:
            return findKthElement(nums1, nums2, (n1 + n2) // 2)
        

# Simple merge algorithm.
class SolutionSimple:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = []
        p1, p2 = 0, 0
        while p1 < len(nums1) or p2 < len(nums2):
            if p1 == len(nums1):
                nums.append(nums2[p2])
                p2 += 1
            elif p2 == len(nums2):
                nums.append(nums1[p1])
                p1 += 1
            elif nums1[p1] < nums2[p2]:
                nums.append(nums1[p1])
                p1 += 1
            else:
                nums.append(nums2[p2])
                p2 += 1
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        else:
            return nums[len(nums) // 2]
