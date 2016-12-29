# percentage: 38.26%
# Log n solution.
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_list = []
        if not nums1:
            merged_list = nums2
        elif not nums2:
            merged_list = nums1
        else:
            idx1 = 0
            idx2 = 0
            while idx1 < len(nums1) or idx2 < len(nums2):
                if idx1 == len(nums1):
                    merged_list.append(nums2[idx2])
                    idx2 += 1
                elif idx2 == len(nums2):
                    merged_list.append(nums1[idx1])
                    idx1 += 1
                else:
                    if nums1[idx1] < nums2[idx2]:
                        merged_list.append(nums1[idx1])
                        idx1 += 1
                    else:
                        merged_list.append(nums2[idx2])
                        idx2 += 1

        l = len(merged_list)
        if l % 2 == 0:
            return (merged_list[l/2-1] + merged_list[l/2])/2.0
        else:
            return merged_list[l/2]
            
        
