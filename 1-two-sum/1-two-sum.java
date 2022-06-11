import java.util.HashMap;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int complement;
        
        // populate hash map for quick look-up
        HashMap<Integer, Integer> hmap = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            complement = target - nums[i];
            
            // check if complement is in hash map.
            if (hmap.containsKey(complement)) {
                return new int[] {i, hmap.get(complement)};
            }
            
            hmap.put(nums[i], i);
        }
        
        return null;
    }
}