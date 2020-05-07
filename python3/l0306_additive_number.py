class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def is_additive(n1, n2, num):
            if not num:
                return True
            

            for i in range(1, len(num)+1):
                if num[0] == '0' and i > 1:
                    break
                if n1 + n2 == int(num[:i]):
                    if is_additive(n2, int(num[:i]), num[i:]):
                        return True
            return False
    
        for i in range(1, len(num)-1):
            if num[0] == '0' and i > 1:
                break
            for j in range(i+1, len(num)):
                if num[i] == '0' and j > i + 1:
                    break
                if is_additive(int(num[:i]), int(num[i:j]), num[j:]):
                    return True
        return False
