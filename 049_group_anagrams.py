class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        anagram_map = defaultdict(list)
        for s in strs:
            signature = ''.join(sorted(s))
            anagram_map[signature].append(s)
        return anagram_map.values()

