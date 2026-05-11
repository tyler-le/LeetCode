class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        n = len(arr)
        prev_dir = None
        UP, DOWN = 0, 1
        cnt = 1
        res = 1

        for i in range(1, n):
            prev = arr[i-1]
            curr = arr[i]

            if prev_dir == None:
                if prev < curr: 
                    prev_dir = UP
                    cnt = 2
                elif prev > curr:
                    prev_dir = DOWN
                    cnt = 2

            elif prev_dir == DOWN:
                if prev > curr: 
                    cnt = 2
                elif prev == curr:
                    cnt = 1
                else: 
                    cnt+=1
                    prev_dir = UP

            else:
                if prev < curr: 
                    cnt = 2
                elif prev == curr:
                    cnt = 1
                else: 
                    cnt+=1
                    prev_dir = DOWN
            
            res = max(res, cnt)

        return res

