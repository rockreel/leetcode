class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isSimpleInteger(s):
            if s and s[0] in '+-':
                s = s[1:]
            if not s:
                return False
            return set(s) <= set('0123456789')
        
        def isSimpleFloat(s):
            if s and s[0] in '+-':
                s = s[1:]
            if not s:
                return False
            if s.find('.') != s.rfind('.'):
                return False
            if s == '.':
                return False
            return set(s) <= set('0123456789.')

        s = s.strip()
        i = s.find('e')
        if i == -1:
            return isSimpleFloat(s)
        else:
            return isSimpleFloat(s[:i]) and isSimpleInteger(s[i+1:])

