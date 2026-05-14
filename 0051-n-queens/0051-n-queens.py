class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        dedup = set()

        def construct_output(queens):
            out = [["." for _ in range(n)] for _ in range(n)]
            for (i,j) in queens:
                out[i][j] = "Q"

            for i in range(len(out)):
                x = "".join(out[i])
                out[i] = x

            return out

        def backtrack(index, used_rows, used_cols, used_diag, used_anti_diag, placed_queens):
            nonlocal used

            if index == n:
                output = construct_output(placed_queens)
                if "".join(output) in dedup: return
                dedup.add("".join(output))
                res.append(output)
                return

            for y in range(n):
                x = index
                if x in used_rows or y in used_cols or x-y in used_diag or x+y in used_anti_diag:
                    continue

                # make choice
                placed_queens.append((x,y))
                used_rows.add(x)
                used_cols.add(y)
                used_diag.add(x-y)
                used_anti_diag.add(x+y)
                
                # recurse
                backtrack(index + 1, used_rows, used_cols, used_diag, used_anti_diag, placed_queens)

                # undo 
                placed_queens.pop()
                used_rows.remove(x)
                used_cols.remove(y)
                used_diag.remove(x-y)
                used_anti_diag.remove(x+y)
        

        
        available_cells = set()
        for i in range(n):
            for j in range(n):
                available_cells.add((i,j))

        used = set()
        backtrack(0, set(), set(), set(), set(), [])
        return res

        