from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid_ip(s):
            if not s:
                return False
            if s == '0':
                return True
            if s[0] == '0':
                return False
            return int(s) >= 1 and int(s) <= 255
        
        def find_ip(s, k, ip, result):
            if k == 4 and not s:
                result.append(ip)
                return
            for i in range(1, len(s)+1):
                if is_valid_ip(s[:i]):
                    find_ip(s[i:], k + 1, ip + [s[:i]], result)
        result = []
        find_ip(s, 0, [], result)
        return ['.'.join(r) for r in result]