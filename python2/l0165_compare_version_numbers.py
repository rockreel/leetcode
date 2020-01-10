class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        versions1 = version1.split('.')
        versions2 = version2.split('.')
        from itertools import izip_longest
        for v1, v2 in izip_longest(versions1, versions2, fillvalue='0'):
            if int(v1) > int(v2):
                return 1
            elif int(v1) < int(v2):
                return -1
        return 0

