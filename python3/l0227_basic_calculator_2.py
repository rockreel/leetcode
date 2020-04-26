class Solution:
    def calculate(self, s: str) -> int:
        s = '+' + s
        tokens = []
        i, j = 0, 0
        while j < len(s):
            while j < len(s) and s[j] == ' ':
                j += 1
            if j == len(s):
                break
            op = s[j]
            i = j + 1
            j += 1
            while i < len(s) and s[i] == ' ':
                i += 1
                j += 1
            while j < len(s) and s[j] not in ' +-*/':
                j += 1
            num = int(s[i:j])
            if op in '+-':
                tokens.append(op)
                tokens.append(num)
            else:

                if op == '*':
                    tokens[-1] *= num
                else:
                    tokens[-1] //= num
        r = 0
        for i in range(0, len(tokens), 2):
            if tokens[i] == '+':
                r += tokens[i+1]
            else:
                r -= tokens[i+1]
        return r
