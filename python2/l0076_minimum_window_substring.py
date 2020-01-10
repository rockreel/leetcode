class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        letter_to_count = defaultdict(int)
        letter_to_count_ref = defaultdict(int)
        for c in t:
            letter_to_count_ref[c] += 1
        letters_found = 0
        letters_found_to_meet = len(letter_to_count_ref.keys())
        start, end = 0, 0
        min_start, min_end = -1, -1
        min_len = len(s) + 1
        while end < len(s):
            found_subwindow = False
            # Front pointer scan.
            while letters_found < letters_found_to_meet and end < len(s):
                if s[end] in letter_to_count_ref:
                    letter_to_count[s[end]] += 1
                    if letter_to_count[s[end]] == letter_to_count_ref[s[end]]:
                        letters_found += 1
                end += 1
            # Back pointer scan.
            while letters_found == letters_found_to_meet and start < len(s):
                found_subwindow = True
                if s[start] in letter_to_count_ref:
                    letter_to_count[s[start]] -= 1
                    if letter_to_count[s[start]] == letter_to_count_ref[s[start]] - 1:
                        letters_found -= 1
                start += 1
            # Compare min lenth.
            if found_subwindow and end - start + 1 < min_len:
                min_start = start - 1
                min_end = end
                min_len = min_end - min_start
        return s[min_start:min_end]

