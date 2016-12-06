# percentage: 85.79%
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        def check_overflow(sign, result):
            if sign == 1 and result > 2147483647:
                return 2147483647
            if sign == -1 and result > 2147483648:
                return -2147483648
            return sign*result
            
        result = 0
        sign = 1
        has_sign = False
        skip_space = True
        digit_set = set('0123456789')
        
        for c in str:
            if c == ' ' and skip_space:
                continue
            
            skip_space = False
            if c == '+':
                if not has_sign:
                    has_sign = True
                    continue
                else:
                    return check_overflow(sign, result)
                    
            if c == '-':
                if not has_sign:
                    sign = -1
                    has_sign = True
                    continue
                else:
                    return check_overflow(sign, result)
                    
            if c not in digit_set:
                return check_overflow(sign, result)
            
            result = result * 10 + ord(c) - 48
            
        return check_overflow(sign, result)
