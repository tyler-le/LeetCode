
class Solution {
    public int maxSubArray(int[] nums) {
        // we will use kadanes algo
        // this vid helped me a lot https://www.youtube.com/watch?v=jnoVtCKECmQ
        
        // set the max to the first
        int max_sum = nums[0];
        int curr_sum = max_sum;
        
        for (int i = 1; i < nums.length; i++) {            
            // after each element, we will choose to EITHER add it to the current sum or to start a new subarray
            // if adding nums[i] to currSum is bigger than nums[i] alone, we will set that to currSum
            // if restarting subarray is better, we will set only nums[i] to currSum (basically restart sum)
            curr_sum = Math.max(nums[i] + curr_sum, nums[i]);
            
            // then we will keep the max of currSum and max 
            max_sum = Math.max(curr_sum, max_sum);
        }
        
        return max_sum;
    }
}