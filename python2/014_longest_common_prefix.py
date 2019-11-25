# Reduce version.
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def common_pefix(s1, s2):
            chars = []
            for c1, c2 in zip(s1, s2):
                if c1 == c2:
                    chars.append(c1)
                else:
                    break
            return ''.join(chars)
        
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        return reduce(common_pefix, strs)
        
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
