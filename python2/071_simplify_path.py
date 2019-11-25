class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        folders = [f for f in path.split('/') if f]
        for f in folders:
            if f == '.':
                continue
            elif f == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(f)
        return '/' + '/'.join(stack)

