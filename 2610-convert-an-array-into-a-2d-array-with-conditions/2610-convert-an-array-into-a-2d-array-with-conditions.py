class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        
        # 4 - 1
        # 3 - 2 
        # 2 - 1
        # 1 - 3
        
        counts = Counter(nums)
        res = [[] for _ in range(max(counts.values()))]
        
        for x, freq in counts.items():
            for i in range(freq):
                res[i].append(x)        
        
        return res
    