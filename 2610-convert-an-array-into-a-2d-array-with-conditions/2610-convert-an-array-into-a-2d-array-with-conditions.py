class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        # val 1 : occurrences 3
        # val 2 : occurrences 1
        # val 3 : occurrences 2
        
        
        hmap = Counter(nums)
        res = [[] for _ in range(max(hmap.values()))]
        
        for num, occ in hmap.items():
            for i in range(occ):
                res[i].append(num)
        return res
        
        
        
        