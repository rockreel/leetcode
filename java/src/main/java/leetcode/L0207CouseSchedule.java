package leetcode;

import java.util.*;

public class L0207CouseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
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
        
        List<Integer> courses = new ArrayList<>();
        while (!queue.isEmpty()) {
            int course = queue.poll();
            courses.add(course);

            for (int j = 0; j < numCourses; j++) {
                if (prereqMap[course][j] == 1) {
                    indegrees[j]--;
                    if (indegrees[j] <= 0) {
                        queue.add(j);
                    }
                }
            }
        }
        return courses.size() == numCourses;
    }
    
    public boolean canFinishMap(int numCourses, int[][] prerequisites) {
        Map<Integer, Integer> indegrees = new HashMap<>();
        Map<Integer, List<Integer>> prereqToCouses = new HashMap<>();
        for (int i = 0; i < prerequisites.length; i++) {
            int c = prerequisites[i][0];
            int p = prerequisites[i][1];
            if (!indegrees.containsKey(c)) {
                indegrees.put(c, 0); 
            }
            indegrees.put(c, indegrees.get(c) + 1);
            if (!prereqToCouses.containsKey(p)) {
                prereqToCouses.put(p, new ArrayList<Integer>());
            } 
            prereqToCouses.get(p).add(c);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < numCourses; i++) {
            if (!indegrees.containsKey(i) || indegrees.get(i) == 0) {
                queue.add(i);
            }
        }
        
        List<Integer> courses = new ArrayList<>();
        while (!queue.isEmpty()) {
            int course = queue.poll();
            courses.add(course);
            if (!prereqToCouses.containsKey(course)) {
                continue;
            }
            for (int c : prereqToCouses.get(course)) {
                indegrees.put(c, indegrees.get(c) - 1);
                if (indegrees.get(c) <= 0) {
                    queue.add(c);
                }
            }
        }
        return courses.size() == numCourses;
    }
}
