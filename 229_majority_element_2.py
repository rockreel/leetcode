class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m1, m2 = None, None
        count1, count2 = 0, 0
        for n in nums:
            if n == m1:
                count1 += 1
            elif n == m2:
                count2 += 1
            elif count1 == 0:
                m1 = n
                count1 += 1
            elif count2 == 0:
                m2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        
        count1, count2 = 0, 0
        for n in nums:
            if n == m1:
                count1 += 1
            elif n == m2:
                count2 += 1
                
        result = []
        if count1 > len(nums)/3:
            result.append(m1)
        if count2 > len(nums)/3:
            result.append(m2)
            
        return result

