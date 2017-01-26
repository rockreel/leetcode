class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        repeated_sequences = set()
        existing_sequences = set()
        for i in range(len(s)-9):
            seq = s[i:i+10]
            if seq in existing_sequences:
                repeated_sequences.add(seq)
            else:
                existing_sequences.add(seq)
        return list(repeated_sequences)

