from functools import lru_cache

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        @lru_cache(None)
        def count_vowel(start, n):
            if start == '':
                return count_vowel('a', n) + count_vowel('e', n) + count_vowel('i', n) + count_vowel('o', n) + count_vowel('u', n)
            if n == 1:
                return 1
            if start == 'a':
                return count_vowel('e', n-1)
            if start == 'e':
                return count_vowel('a', n-1) + count_vowel('i', n-1)
            if start == 'i':
                return count_vowel('a', n-1) + count_vowel('e', n-1) + count_vowel('o', n-1) + count_vowel('u', n-1)
            if start == 'o':
                return count_vowel('i', n-1) + count_vowel('u', n-1)
            if start == 'u':
                return count_vowel('a', n-1)
            return 0

        return count_vowel('', n) % (10**9 + 7)
                