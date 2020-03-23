class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or open_close_map[stack.pop()] != c:
                    return False
        return len(stack) == 0