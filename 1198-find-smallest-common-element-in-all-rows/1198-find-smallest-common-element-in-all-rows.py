class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hmap = defaultdict(int)
        n = len(mat)

        for row in mat:
            for x in row:
                hmap[x]+=1
        
        for x in mat[0]:
            if hmap[x] == n: return x
        
        return -1
        
        