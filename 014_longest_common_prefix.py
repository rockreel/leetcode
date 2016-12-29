# precentage: 63.92%
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        i = 0
        prefix = []
        
        while i < len(strs[0]):
            for s in strs[1:]:
                if i >= len(s) or strs[0][i] != s[i]:
                    return ''.join(prefix)
            prefix.append(strs[0][i])
            i += 1
            
        return ''.join(prefix)
