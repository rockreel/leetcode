class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            raise Exception('Divided by Zero!')
             
        dividend_positive = True
        if dividend < 0:
            dividend_positive = False
        
        divisor_positive = True
        if divisor < 0:
            divisor_positive = False
        
        if ((dividend_positive and divisor_positive) or
            (not dividend_positive and not divisor_positive)):
            init_substractor = divisor
            init_multiple = 1
        else:
            init_substractor = -divisor
            init_multiple = -1
            
        multiple = init_multiple
        substractor = init_substractor
        result = 0
        while ((dividend_positive and dividend > 0) or
               (not dividend_positive and dividend < 0)):
            if ((dividend_positive  and dividend - substractor - substractor > 0) or
                (not dividend_positive and dividend - substractor - substractor < 0)):
                substractor += substractor
                multiple += multiple
            else:
                new_dividend = dividend - substractor
                # Check overflow.
                if result > 2147483647 - multiple:
                    new_result = 2147483647
                elif result < -2147483648 - multiple:
                    new_result = -2147483648
                else:
                    new_result = result + multiple
                    
                if ((dividend_positive and new_dividend >= 0) or
                    (not dividend_positive and new_dividend <= 0)):
                    dividend = new_dividend
                    result = new_result
                    multiple = init_multiple
                    substractor = init_substractor
                else:
                    break
            
        return result

