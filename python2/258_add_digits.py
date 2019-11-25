class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add_digits(n):
            result = 0
            while n > 0:
                result += n%10
                n /= 10
            return result
        
        while num > 9:
            num = add_digits(num)
        return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num < 10:
            return num
        return num-9*((num-1)/9)

