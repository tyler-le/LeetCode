class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # count the frequencies and take the min element with count len(mat)
        cnt = defaultdict(int)
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                cnt[mat[i][j]]+=1
        
        for num in mat[0]:
            if cnt[num] == len(mat):
                return num
        
        return -1