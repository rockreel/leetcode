from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_to_course_map = defaultdict(list)
        course_prereq_count = [0] * numCourses
        for p in prerequisites:
            prereq_to_course_map[p[1]].append(p[0])
            course_prereq_count[p[0]] += 1
        queue = [course for course, count in enumerate(course_prereq_count) if count == 0]
        courses = []
        while queue:
            course = queue.pop(0)
            courses.append(course)
            for c in prereq_to_course_map[course]:
                course_prereq_count[c] -= 1
                if course_prereq_count[c] == 0:
                    queue.append(c)
        if sum(course_prereq_count) == 0:
            return courses
        else:
            return []