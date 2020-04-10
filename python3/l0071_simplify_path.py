class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return ''
        p1, p2 = 0, -1
        stack = []
        while p1 < len(path):
            while p1 < len(path) and path[p1] != '/':
                p1 += 1
            seg = path[p2+1:p1]
            if seg == '..':
                if stack:
                    stack.pop()
            elif seg and seg != '.':
                stack.append(seg)
            p2 = p1
            p1 += 1
        return '/' + '/'.join(stack)