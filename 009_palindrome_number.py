# percentage: 32.09%
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x  < 0:
            return False
            
        digits = []
        while x > 0:
            digits.append(x%10)
            x /= 10
        
        i, j = 0, len(digits) - 1
        
        while i < j:
            if digits[i] != digits[j]:
                return False
            i += 1
            j -= 1
                
        return True
