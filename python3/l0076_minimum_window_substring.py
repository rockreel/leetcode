from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        char_count_t = defaultdict(int)
        for c in t:
            char_count_t[c] += 1
        char_count = defaultdict(int)
        letters_found = 0  # Number of unique letters found in t.
        letters_to_find = len(char_count_t.keys())
        p1, p2 = 0, 0
        min_substr = ''
        while p2 < len(s):
            while p2 < len(s) and letters_found < letters_to_find:
                if s[p2] in char_count_t:
                    char_count[s[p2]] += 1
                    if char_count[s[p2]] == char_count_t[s[p2]]:
                        letters_found += 1
                p2 += 1
            if letters_found < letters_to_find:
                break
            while p1 < len(s) and letters_found == letters_to_find:
                if s[p1] in char_count_t:
                    char_count[s[p1]] -= 1
                    if char_count[s[p1]] < char_count_t[s[p1]]:
                        letters_found -= 1
                p1 += 1

            if not min_substr or p2 - p1 + 1 < len(min_substr):
                min_substr = s[p1-1:p2]
 
        return min_substr