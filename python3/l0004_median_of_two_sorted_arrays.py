from typing import List

# Recursion.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def findKthElement(nums1: List[int], nums2: List[int], k) -> float:
            if not nums1:
                return nums2[k-1]
            elif not nums2:
                return nums1[k-1]
            elif k == 1:
                return min(nums1[0], nums2[0])

            m1 = nums1[k//2-1] if k//2 - 1 < len(nums1) else float("inf")
            m2 = nums2[k//2-1] if k//2 - 1 < len(nums2) else float("inf")
            if m1 < m2:
                return findKthElement(nums1[k//2:], nums2, k - k//2)
            else:
                return findKthElement(nums1, nums2[k//2:], k - k//2)

        n = len(nums1) + len(nums2)
        if n % 2 == 0:
            return (findKthElement(nums1, nums2, n//2) + findKthElement(nums1, nums2, n//2+1)) / 2.0
        else:
            return findKthElement(nums1, nums2, n//2 + 1)
        

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
