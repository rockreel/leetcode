package leetcode;

import java.util.*;

public class L0210CouseSchedule2 {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] indegrees = new int[numCourses];
        int[][] prereqMap = new int[numCourses][numCourses]; // If i is prerequisite of j, then prereqMap[i][j] = 1.
        for (int i = 0; i < prerequisites.length; i++) {
            int c = prerequisites[i][0];
            int p = prerequisites[i][1];
            prereqMap[p][c] = 1;
            indegrees[c]++;
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (indegrees[i] == 0) {
                queue.add(i);
            }
        }
        
        int[] courses = new int[numCourses];
        int count = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            courses[count] = course;
            count++;
            for (int j = 0; j < numCourses; j++) {
                if (prereqMap[course][j] == 1) {
                    indegrees[j]--;
                    if (indegrees[j] <= 0) {
                        queue.add(j);
                    }
                }
            }
        }

        if (count == numCourses) {
            return courses;
        }
        return new int[0];
    }
    
    
}
