class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # fixed window of length k
        l, n = 0, len(blocks)
        white_count, black_count, res = 0, 0, math.inf

        for r in range(n):
            # add to window
            if blocks[r] == "B": black_count+=1
            else: white_count+=1

            # shrink window
            while r - l + 1 > k:
                if blocks[l] == "B": black_count-=1
                else: white_count-=1
                l+=1
            
            # record result
            if r-l+1 == k:
                res = min(res, white_count)
        
        return res


            