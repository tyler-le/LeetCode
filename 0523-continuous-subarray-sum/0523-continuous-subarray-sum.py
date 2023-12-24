class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # map (prefix_sum % k : i)
        # if the mod is already seen previously, this implies we have a valid subarray
        # len(subarray) >= 2 and sum(subarr) % k == 0
        
        hmap = collections.defaultdict(int)
        prefix_sum = 0
        hmap[0] = -1
        
        for i, num in enumerate(nums):

            prefix_sum+=num
            r = prefix_sum % k
            
            if r not in hmap:
                hmap[r] = i
            
            elif i - hmap[r] > 1: 
                return True
                        
        return False