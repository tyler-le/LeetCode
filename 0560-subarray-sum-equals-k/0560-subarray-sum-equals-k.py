class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Striver's Explanation: https://www.youtube.com/watch?v=xvNwoz-ufXA
        pre_sum = 0
        hmap = collections.defaultdict(int)
        hmap[0] = 1 # map prefix sum : freq
        res = 0
        
        for num in nums:
            pre_sum+=num
            if pre_sum - k in hmap:
                res+=hmap[pre_sum - k]
            
            hmap[pre_sum]+=1
            
        return res