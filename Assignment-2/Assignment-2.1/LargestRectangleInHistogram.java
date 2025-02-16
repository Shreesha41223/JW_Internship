import java.util.*;

class LargestRectangleInHistogram {
    public int largestRectangleArea(int[] heights) {
        Stack<int[]> stack = new Stack<>();
        stack.push(new int[] { 0, -1 });
        int maxArea = 0;

        for (int i = 0; i < heights.length; i++) {
            int start = i;
            while (stack.peek()[1] > heights[i]) {
                int[] top = stack.pop();
                maxArea = Math.max(maxArea, top[1] * (i - top[0]));
                start = top[0];
            }
            stack.push(new int[] { start, heights[i] });
        }

        while (stack.peek()[1] != -1) {
            int[] top = stack.pop();
            maxArea = Math.max(maxArea, top[1] * (heights.length - top[0]));
        }

        return maxArea;
    }
}