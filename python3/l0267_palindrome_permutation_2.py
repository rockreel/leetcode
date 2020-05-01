class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        # write your code here
        def permutation(letters):
            if not letters:
                return [[]]
            prev = ''
            result = []
            for i, l in enumerate(letters):
                if l != prev:
                    for r in permutation(letters[:i] + letters[i+1:]):
                        result.append([l] + r)
                    prev = l
            return result
        
        s = sorted(s)
        middle = ''
        candidates = []
        i = 0
        while i < len(s):
            next_c = s[i+1] if i + 1 < len(s) else ''
            if s[i] != next_c:
                if not middle:
                    middle = s[i]
                    i += 1
                else:
                    return []
            else:
                candidates.append(s[i])
                i += 2
        palindromes = []
        for p in permutation(candidates):
            p = ''.join(p)
            palindromes.append(p + middle + p[::-1])
        return palindromes