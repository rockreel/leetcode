# BFS topological sorting.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict
        
        # From prerequisite course to courese depend on it.
        prerequisite_map = defaultdict(list)
        for c, p in prerequisites:
            prerequisite_map[p].append(c)
            
        # Count num prerequisite each course has.
        prerequisite_couter = [0] * numCourses
        for c, _ in prerequisites:
            prerequisite_couter[c] += 1
        
        # Topological sort.
        queue = [
            c for c, n in enumerate(prerequisite_couter) if n == 0]
        course_order = [
            c for c, n in enumerate(prerequisite_couter) if n == 0]
        while queue:
            course = queue.pop(0)
            for p in prerequisite_map[course]:
                prerequisite_couter[p] -= 1
                if prerequisite_couter[p] == 0:
                    queue.append(p)
                    course_order.append(p)

        return len(course_order) == numCourses

# DFS checking loops and remove visited course from total courses.
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def has_loop(course, prerequisite_map, visited, courses):
            # DFS through graph started at course and
            # remove course from total courses.
            if course in visited:
                return True
            visited.add(course)
            if course in courses:
                courses.remove(course)
            for c in prerequisite_map[course]:
                if has_loop(c, prerequisite_map, visited, courses):
                    return True
            visited.remove(course)
            return False
            
        from collections import defaultdict
        prerequisite_map = defaultdict(list)
        for c, p in prerequisites:
            prerequisite_map[c].append(p)
        courses = set(range(numCourses))
        while courses:
            course = courses.pop()
            if has_loop(course, prerequisite_map, set(), courses):
                return False

        return True
