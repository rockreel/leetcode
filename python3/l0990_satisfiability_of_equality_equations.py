from collections import defaultdict

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        eq_map = defaultdict(list)
        vars = set()
        var_group = dict()
        i = 0
        for eq in equations:
            if eq[1] == '=':
                eq_map[eq[0]].append(eq[3])
                eq_map[eq[3]].append(eq[0])
            vars.add(eq[0])
            vars.add(eq[3])
        
        while vars:
            var = vars.pop()
            queue = [var]
            visited = set()
            while queue:
                v = queue.pop(0)
                if v in vars:
                  vars.remove(v)
                var_group[v] = i
                for o in eq_map[v]:
                    if o not in visited:
                        queue.append(o)
                        visited.add(o)
            i += 1
            
        for eq in equations:
            if eq[1] == '!':
                if var_group[eq[0]] == var_group[eq[3]]:
                    return False
        return True
