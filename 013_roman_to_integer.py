# percentage: 20.37%
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and s[i:i+2] == 'IV':
                result += 4
                i += 2
            elif i + 1 < len(s) and s[i:i+2] == 'IX':
                result += 9
                i += 2
            elif i + 1 < len(s) and s[i:i+2] == 'XL':
                result += 40
                i += 2
            elif i + 1 < len(s) and s[i:i+2] == 'XC':
                result += 90
                i += 2
            elif i + 1 < len(s) and s[i:i+2] == 'CD':
                result += 400
                i += 2
            elif i + 1 < len(s) and s[i:i+2] == 'CM':
                result += 900
                i += 2
            elif s[i] == 'I':
                result += 1
                i += 1
            elif s[i] == 'V':
                result += 5
                i += 1
            elif s[i] == 'X':
                result += 10
                i += 1
            elif s[i] == 'L':
                result += 50
                i += 1
            elif s[i] == 'C':
                result += 100
                i += 1
            elif s[i] == 'D':
                result += 500
                i += 1
            elif s[i] == 'M':
                result += 1000
                i += 1
        return result

