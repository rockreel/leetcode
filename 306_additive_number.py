class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def is_additive_num(n1, n2, num):
            if len(n1) > 1 and n1[0] == '0':
                return False
            if len(n2) > 1 and n2[0] == '0':
                return False
            if not num:
                return True
            for i in range(1, len(num)+1):
                n = num[:i]
                if int(n1) + int(n2) == int(n) and is_additive_num(n2, n, num[i:]):
                    return True
            return False
            
        for i in range(1, len(num)-1):
            for j in range(i+1, len(num)):
                if is_additive_num(num[:i], num[i:j], num[j:]):
                    return True
        return False

