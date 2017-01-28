# DFS and remove visited course from total courses.
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
