class Solution:
    """
    @param s: the given string
    @return: if the starting player can guarantee a win
    """
    def canWin(self, s):
        # write your code here
        for i in range(len(s)-1):
            if s[i:i+2] == '++':
                flipped = s[:i] + '--' + s[i+2:]
                if not self.canWin(flipped):
                    return True
        return False
