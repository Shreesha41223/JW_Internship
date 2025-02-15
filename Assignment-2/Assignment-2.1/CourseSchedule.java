import java.util.*;

class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        List<List<Integer>> adj = new ArrayList<>();
        int[] inDegree = new int[numCourses];

        for (int i = 0; i < numCourses; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] preReq : prerequisites) {
            adj.get(preReq[1]).add(preReq[0]);
            inDegree[preReq[0]]++;
        }

        Queue<Integer> queue = new LinkedList<Integer>();

        for (int i = 0; i < numCourses; i++) {
            if (inDegree[i] == 0) {
                queue.add(i);
            }
        }

        int coursesCompleted = 0;
        while (!queue.isEmpty()) {
            int course = queue.poll();
            coursesCompleted++;
            for (int nextCourse : adj.get(course)) {
                if (--inDegree[nextCourse] == 0) {
                    queue.add(nextCourse);
                }
            }
        }
        return numCourses == coursesCompleted;
    }
}