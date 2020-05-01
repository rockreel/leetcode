class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        l = []
        for s in strs:
            ss = []
            for i in range(len(s)):
                if s[i] == ':':
                    ss.append('::')
                elif s[i] == ';':
                    ss.append(';;')
                else:
                    ss.append(s[i])
            l.append(''.join(ss))
        return ':;'.join(l)

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        l = []
        ss = []
        i = 0
        while i < len(str):
            if str[i] == ':':
                if str[i:i+2] == '::':
                    ss.append(':')
                elif str[i:i+2] == ':;':
                    l.append(''.join(ss))
                    ss = []
                i += 2
            elif str[i] == ';':
                ss.append(';')
                i += 2
            else:
                ss.append(str[i])
                i += 1
        l.append(''.join(ss))
        return l