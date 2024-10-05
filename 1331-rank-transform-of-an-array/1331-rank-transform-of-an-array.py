class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = list(set(arr))
        nums.sort()
        ranks = {}
        
        for i, num in enumerate(nums):
            if num not in ranks:
                ranks[num] = i+1
                
        res = []
        
        for x in arr:
            res.append(ranks[x])
        
        return res