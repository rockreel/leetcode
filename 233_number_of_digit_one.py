class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 1
        result = 0
        # The part lower than current digit.
        lower_num = 0
        # Total number of digit one under base: 1, 10, 100.
        # n(base) = 10*n(base/10) + base/10
        # n(1) = 0, n(10) = 1, n(100) = 20 ...
        total_one_digits_for_base = 0
        while n > 0:
            curr_digit = n % 10
            if curr_digit > 1:
                result += base  # For 1***.
            elif curr_digit == 1:
                result += lower_num + 1  # For 1***.
            result += curr_digit * total_one_digits_for_base
            
            lower_num += curr_digit * base
            total_one_digits_for_base = 10*total_one_digits_for_base + base
            base *= 10
            n /= 10
            
        return result

