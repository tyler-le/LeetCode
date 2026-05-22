class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        row_cnt = defaultdict(int)
        col_cnt = defaultdict(int)

        n,m = len(picture), len(picture[0])
        res = 0

        for i in range(n):
            for j in range(m):
                if picture[i][j] == "B":
                    row_cnt[i]+=1
                    col_cnt[j]+=1

        for i in range(n):
            for j in range(m):
                res+=picture[i][j] == "B" and row_cnt[i] == 1 and col_cnt[j] == 1

        return res