class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        subset = set(mat[0])
        
        for m in mat[1:]:
            subset = subset.intersection(set(m))
        
        return min(subset) if subset else -1