class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        hmap = defaultdict(int)
        res = []
        
        for row in mat:
            my_set = set(row)
            for x in my_set:
                hmap[x]+=1
        
        for k, v in hmap.items():
            if v == len(mat):
                res.append(k)
        res.sort()
        return res[0] if res else -1