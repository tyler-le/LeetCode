class Solution {
    public int search(int[] nums, int target) {
        int low = 0;
        int high = nums.length-1;
        
        return binary_search(low, high, target, nums);
    }
    
    int binary_search(int low, int high, int target, int[] nums) {
        if (low > high) return -1;
        int mid = low + (high-low) / 2;
        if (nums[mid] < target) return binary_search(mid+1, high, target, nums);
        else if (nums[mid] > target) return binary_search(low, mid-1, target, nums); 
        return mid;
    }
    
    
}