class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or not num2:
            return ''
        
        result = 0
        base1 = 1
        for n1 in num1[::-1]:
            if n1 == '-':
                continue
            base2 = 1
            for n2 in num2[::-1]:
                if n2 == '-':
                    continue
                result += (ord(n2) - 48) * (ord(n1) - 48) * base1 * base2
                base2 *= 10
            base1 *= 10
        
        if ((num1[0] == '-' and num2[0] != '-') or
            (num1[0] != '-' and num2[0] =='-')):
            return '-' + str(result)
        else:
            return str(result)


