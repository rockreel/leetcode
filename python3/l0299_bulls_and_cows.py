class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        char_count = [0] * 10
        a, b = 0, 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                a += 1
            else:
                char_count[int(secret[i])] += 1
        for i in range(len(guess)):
            if secret[i] != guess[i]:
                if char_count[int(guess[i])] > 0:
                    b += 1
                    char_count[int(guess[i])] -= 1
        return '%sA%sB' % (a, b)
