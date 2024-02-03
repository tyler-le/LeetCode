class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hmap = defaultdict(int)
        acc = 0
        hmap[0] = -1
        for i, num in enumerate(nums):
            acc+=num
            r = acc % k
            if r in hmap and i - hmap[r] >= 2: 
                return True
            if r not in hmap: 
                hmap[r] = i
        
        return False