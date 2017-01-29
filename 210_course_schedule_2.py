class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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

        return course_order if len(course_order) == numCourses else []

