class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        # map prefix sum : number of times that prefix sum occurs
        hmap = defaultdict(int)
        hmap[0] += 1
        acc = 0
        res = 0
        
        for i in range(len(nums)):
            acc+=nums[i]
            
            if acc - k in hmap:
                res+=hmap[acc - k]
            
            hmap[acc]+=1
        
        return res
        
        