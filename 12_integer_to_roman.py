# percentage: 33.02%
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        def genDigit(n):
            if n < 4:
                return 'I', n - 1
            elif n < 5:
                return 'IV', n - 4
            elif n < 9:
                return 'V', n - 5
            elif n < 10:
                return 'IX', n - 9
            elif n < 40:
                return 'X', n - 10
            elif n < 50:
                return 'XL', n - 40
            elif n < 90:
                return 'L', n - 50
            elif n < 100:
                return 'XC', n - 90
            elif n < 400:
                return 'C', n - 100
            elif n < 500:
                return 'CD', n - 400
            elif n < 900:
                return 'D', n - 500
            elif n < 1000:
                return 'CM', n - 900
            elif n < 4000:
                return 'M', n - 1000
            return '', 0
                
        result = []
        r = num
        
        while r > 0:
            n, r = genDigit(r)
            result.append(n)
            
        return ''.join(result)

