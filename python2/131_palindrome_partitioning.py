class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        
        partitions = []
        for i in range(1, len(s)+1):
            if s[:i] == s[:i][::-1]:  # s[:i] is a palindrome.
                for partition in self.partition(s[i:]):
                    partitions.append([s[:i]] + partition)
                
        return partitions

