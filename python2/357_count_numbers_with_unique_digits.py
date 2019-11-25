class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 10 ** n
        
        num_with_unique_digit = 9
        result = 0
        for k in range(2, n+1):
            num_with_unique_digit *= 9-k+2
            result += num_with_unique_digit
    
        return result + 10

