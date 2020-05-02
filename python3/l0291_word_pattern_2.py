class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        def word_pattern(pattern, str, mapping):
            if not pattern and not str:
                return True
            if not pattern or not str:
                return False
            i, j = 0, 0
            while i < len(pattern) and pattern[i] in mapping:
                word = mapping[pattern[i]]
                if str[j:j+len(word)] != word:
                    
                    return False
                i += 1
                j += len(word)
            pattern = pattern[i:]
            str = str[j:]
            
            if not pattern and not str:
                return True
                
            for i in range(1, len(str)+1):
                if str[:i] in mapping.values():
                    continue
                
                mapping[pattern[0]] = str[:i]
                if word_pattern(pattern[1:], str[i:], mapping):
                    return True
                mapping.pop(pattern[0])
            return False
        return word_pattern(pattern, str, {})

