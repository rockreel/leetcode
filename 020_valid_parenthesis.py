class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        close_to_open_map = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack.pop() != close_to_open_map[c]:
                    return False
        return len(stack) == 0
