class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # val 1 : freq 3
        # val 2 : freq 1
        # val 3 : freq 2
        
        hmap = Counter(nums)
        res = [[] for _ in range(max(hmap.values()))]
        
        for num, freq in hmap.items():
            for i in range(freq):
                res[i].append(num)
                
        return res
        
        
        
        