class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        chars = list(s)
        i, j = 0, len(chars)-1
        while i < j:
            while i < len(chars) and chars[i] not in 'aeiouAEIOU':
                i += 1
            while j >= 0 and chars[j] not in 'aeiouAEIOU':
                j -= 1
            if i < j:
                chars[i], chars[j] = chars[j], chars[i]
                i += 1
                j -= 1
        return ''.join(chars)

