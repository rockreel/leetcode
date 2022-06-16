class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        def canBeRepeatedBy(s, p):
            if len(s) % len(p) != 0:
                return False
            for i in range(0, len(s), len(p)):
                for j in range(len(p)):
                    if s[i+j] != p[j]:
                        return False
            return True
       
        for i in range(len(s)//2):
            if canBeRepeatedBy(s, s[:i+1]):
                return True
        return False