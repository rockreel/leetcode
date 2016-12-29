# percentage: 89.66%
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        digits = []
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1
            
        while x > 0:
            digits.append(x%10)
            x = x / 10
        
        result = 0
        prev_result = 0
        for d in digits:
            result = result*10 +d
            if result > 2**31:  # Fake overflow of 32 bit integer.
                return 0
            else:
                prev_result = result
   
        return sign*result
        

