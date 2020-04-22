class Solution:
    """
    @param str: a string
    @return: return a string
    """
    def reverseWords(self, s):
        # write your code here
        
        def reverse(s, start, end):
            i, j = start, end
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            
        # Reverse whole string.
        s = list(s)
        reverse(s, 0, len(s)-1)

        # Reverse each word.
        word_start, word_end = 0, 0
        while word_end < len(s):
            while word_end < len(s) and s[word_end] != ' ':
                word_end += 1
            reverse(s, word_start, word_end - 1)
            word_end += 1
            word_start = word_end
                
        return ''.join(s)