class FindFirstLastPosition {
    public int[] searchRange(int[] nums, int target) {
        int[] positions = new int[2];
        positions[0] = binarySearch(nums, target, true);
        positions[1] = binarySearch(nums, target, false);
        return positions;
    }

    int binarySearch(int[] nums, int target, boolean searchingStartPosition) {
        int left = 0;
        int right = nums.length - 1;
        int position = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (nums[mid] < target) {
                left = mid + 1;
            } else if (nums[mid] > target) {
                right = mid - 1;
            } else {
                position = mid;
                if (searchingStartPosition) {
                    right = mid - 1;
                } else {
                    left = mid + 1;
                }
            }
        }
        return position;
    }
}