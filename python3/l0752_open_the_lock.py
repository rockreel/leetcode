from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends or target in deadends:
            return - 1
        set_forward = set(['0000'])
        set_backward = set([target])
        visited_forward = set(['0000'])
        visited_backward = set([target])
        deadends = set(deadends)
        depth = 0
        while set_forward and set_backward:
            if set_forward.intersection(set_backward):
                return 2 * depth
            set_forward_next = set([])
            for s in set_forward:
                for i, n in enumerate(s):
                    n = int(n)
                    for d in [-1, 1]:
                        n_next = (n + d) % 10
                        s_next = s[:i] + str(n_next) + s[i+1:]
                        if s_next in set_backward:
                            return 2 * depth + 1
                        if s_next not in deadends and s_next not in visited_forward:
                            set_forward_next.add(s_next)
                            visited_forward.add(s_next)
                        
            set_backward_next = set([])
            for s in set_backward:
                for i, n in enumerate(s):
                    n = int(n)
                    for d in [-1, 1]:
                        n_next = (n + d) % 10
                        s_next = s[:i] + str(n_next) + s[i+1:]
                        if s_next not in deadends and s_next not in visited_backward:
                            set_backward_next.add(s_next)
                            visited_backward.add(s_next)
            
            set_backward = set_backward_next
            set_forward = set_forward_next
            depth += 1

        return -1