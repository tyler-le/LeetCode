class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        hmap = collections.defaultdict(deque)
        res = []
        
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                hmap[i+j].appendleft(nums[i][j])
                        
        for v in hmap.values():
            res+=list(v)
        
        return res
        
