class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        p1, p2 = len(s) - 1, len(t) - 1
        skip1, skip2 = 0, 0
        while p1 >= 0 or p2 >= 0:
            while p1 >= 0:
                if s[p1] == '#':
                    skip1 += 1
                    p1 -= 1
                elif skip1 > 0:
                    skip1 -= 1
                    p1 -= 1
                else:
                    break
            while p2 >= 0:
                if t[p2] == '#':
                    skip2 += 1
                    p2 -= 1
                elif skip2 > 0:
                    skip2 -= 1
                    p2 -= 1
                else:
                    break
            print(p1, p2)
            if p1 < 0 and p2 < 0:
                return True
            if (p1 >= 0 and p2 < 0) or (p1 < 0 and p2 >= 0):
                return False
            if s[p1] != t[p2]:
                return False
            p1 -= 1
            p2 -= 1
        return p1 < 0 and p2 < 0
        
    def backspaceCompareBuildString(self, s: str, t: str) -> bool:
        s0, t0 = [], []
        for c in s:
            if c != '#':
                s0.append(c)
            else:
                if s0:
                    s0.pop()
        for c in t:
            if c != '#':
                t0.append(c)
            else:
                if t0:
                    t0.pop()
        return ''.join(s0) == ''.join(t0)  