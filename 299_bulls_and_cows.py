class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        from collections import defaultdict
        secret_map = defaultdict(int)
        guess_map = defaultdict(int)
        a, b = 0, 0
        for s, g in zip(secret, guess):
            if s == g:
                a += 1
            else:
                secret_map[s] += 1
                guess_map[g] += 1
        for s, count in secret_map.iteritems():
            b += min(count, guess_map[s])
        return '%sA%sB' % (a, b)

