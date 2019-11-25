class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = ''
        if numerator*denominator < 0:
            sign = '-'
            numerator = abs(numerator)
            denominator = abs(denominator)

        digits = []
        integral = numerator / denominator
        numerator = numerator % denominator
        numerator_map = {}
        idx = 0
        while numerator != 0 and numerator not in numerator_map:
            quotient = 10 * numerator / denominator
            residual = 10 * numerator % denominator
            digits.append(str(quotient))
            numerator_map[numerator] = idx
            numerator = residual 
            idx += 1

        if numerator != 0:  # Recursion happened.
            digits.insert(numerator_map[numerator], '(')
            digits.append(')')
            
        if digits:
            return '%s%s.%s' % (sign, integral, ''.join(digits))
        else:
            return '%s%s' % (sign, integral)

