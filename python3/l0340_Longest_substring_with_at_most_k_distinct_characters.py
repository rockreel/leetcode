class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # write your code here
        from collections import defaultdict
        char_count = defaultdict(int)
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            char_count[c] += 1
            while len(char_count.keys()) > k:
                char_count[s[start]] -= 1
                if char_count[s[start]] == 0:
                    char_count.pop(s[start])
                start += 1
            max_len = max(max_len, i-start+1)
        return max_len
