class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        hmap = collections.defaultdict(int)
        res = 0
        
        for num in nums:
            target = k - num
            if hmap[target] > 0:
                hmap[target]-=1
                res+=1
            else:
                hmap[num]+=1
            
        return res
        
        