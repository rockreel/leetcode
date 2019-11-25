class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue = [[s, []]]  # [string to restore, already recovered parts].
        ip_addresses = []
        while queue:
            ip_str, parts = queue.pop(0)
            if len(parts) == 4:
                if not ip_str:
                    ip_addresses.append('.'.join(parts))
                continue
            
            if not ip_str:
                continue
            
            # Use first letter.
            queue.append([ip_str[1:], parts + [ip_str[:1]]])
            
            # Use first 2 letters.
            if len(ip_str) > 1:
                if ip_str[0] == '0':  # '0?' is not a valid ip address part.
                    continue
                queue.append([ip_str[2:], parts + [ip_str[:2]]])
            
            # Use first 3 letters.
            if len(ip_str) > 2:
                if ip_str[0] not in '12':
                    continue
                if ip_str[0] == '2':
                    if ip_str[1] not in '012345':
                        continue
                    if ip_str[1] == '5' and ip_str[2] not in '012345':
                        continue
                queue.append([ip_str[3:], parts + [ip_str[:3]]])
                
        return ip_addresses

