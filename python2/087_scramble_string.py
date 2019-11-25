class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):
            return False
            
        if not s1:
            return True
        
        if len(s1) == 1:
            return s1 == s2
            
        if len(s1) == 2:
            return s1 == s2 or s1 == s2[::-1]
        
        from collections import defaultdict
        letter_count_1 = defaultdict(int)
        letter_count_2 = defaultdict(int)
        letter_count_3 = defaultdict(int)
            
        for i in range(1, len(s1)):
            # Partition s1, s2 at same position.
            letter_count_1[s1[i-1]] += 1
            letter_count_2[s2[i-1]] += 1
            if letter_count_1 == letter_count_2:
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    return True
            # Partition s1, s2 one from start and the other from the end.
            letter_count_3[s2[len(s2)-i]] += 1
            if letter_count_1 == letter_count_3:
                if self.isScramble(s1[:i], s2[len(s2)-i:]) and self.isScramble(s1[i:], s2[:len(s2)-i]):
                    return True
        return False

