class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        tokens1 = [int(v) for v in version1.split('.')]
        tokens2 = [int(v) for v in version2.split('.')]
        i, j = 0, 0
        while i < len(tokens1) or j < len(tokens2):
            v1 = tokens1[i] if i < len(tokens1) else 0
            v2 = tokens2[j] if i < len(tokens2) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            i += 1
            j += 1
        return 0
