class Solution {
    public int[] searchRange(int[] nums, int target) {
        int ind1 = -1;
        int ind2 = -1;

        int low = 0;
        int high = nums.length - 1;

        while (low <= high) {
            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                ind1 = mid;
                high = mid - 1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }

        }

        low = 0;
        high = nums.length - 1;
        while (low <= high) {

            int mid = low + (high - low) / 2;

            if (nums[mid] == target) {
                ind2 = mid;
                low = mid + 1;
            } else if (nums[mid] < target) {
                low = mid + 1;
            } else {
                high = mid - 1;
            }

        }

        return new int[] { ind1, ind2 };
    }
}