from collections import Counter

class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        letter_count = Counter(s)
        single_count = 0
        for l, c in letter_count.items():
            if c % 2 != 0:
                single_count += 1
        return single_count <= 1