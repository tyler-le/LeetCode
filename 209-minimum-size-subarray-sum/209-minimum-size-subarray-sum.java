class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int min_length = Integer.MAX_VALUE;
        int curr_sum = nums[0];
        int start = 0;
        int end = 0;
        
        while (end < nums.length) {
            
            if (curr_sum >= target) {
                if (end - start + 1 < min_length) min_length = end - start + 1;
                curr_sum = curr_sum - nums[start];
                start++;
            }
            
            else {
                end++;
                if (end < nums.length) curr_sum += nums[end];
            }
        }
        
        return min_length == Integer.MAX_VALUE ? 0 : min_length;
    }
}