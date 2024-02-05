class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hmap = defaultdict(int)
        hmap[0] = 1

        prefix_sum = 0
        res = 0
        
        for num in nums:
            prefix_sum+=num
            
            res+=hmap[prefix_sum - goal]
            
            hmap[prefix_sum]+=1
        
        return res