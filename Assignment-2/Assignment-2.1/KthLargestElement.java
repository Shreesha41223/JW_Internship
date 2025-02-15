import java.util.*;

class KthLargestElement {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();

        for (int i = 0; i < k; i++)
            pq.add(nums[i]);

        for (int j = k; j < nums.length; j++) {
            if (nums[j] > pq.peek()) {
                pq.poll();
                pq.add(nums[j]);
            }
        }
        return pq.peek();
    }
}