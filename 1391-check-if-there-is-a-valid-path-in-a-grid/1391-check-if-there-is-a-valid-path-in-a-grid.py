class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        street_1 = {
            (-1,0): [],
            (1,0): [],
            (0,-1): [1,4,6],
            (0,1): [1,3,5]
        }

        street_2 = {
            (-1,0): [2,3,4],
            (1,0): [2,5,6],
            (0,-1): [],
            (0,1): []
        }

        street_3 = {
            (-1,0): [],
            (1,0): [2,5,6],
            (0,-1): [1,4],
            (0,1): []
        }

        street_4 = {
            (-1,0): [],
            (1,0): [2,5,6],
            (0,-1): [],
            (0,1): [1,3,5]
        }

        street_5 = {
            (-1,0): [2,3,4],
            (1,0): [],
            (0,-1): [1,4],
            (0,1): []
        }

        street_6 = {
            (-1,0): [2],
            (1,0): [],
            (0,-1): [],
            (0,1): [1,3,5]
        }

        def get_compatible_streets(street, street2, dir):
            hmap = None
            if street == 1:
                hmap = street_1
            elif street == 2:
                hmap = street_2
            if street == 3:
                hmap = street_3
            elif street == 4:
                hmap = street_4
            if street == 5:
                hmap = street_5
            elif street == 6:
                hmap = street_6
            
            return hmap[dir]



        q = deque([(0, 0,grid[0][0])]) # (i,j,street)
        visited = set([(0,0)])
        n, m = len(grid), len(grid[0])

        while q:
            popped_x, popped_y, popped_street = q.popleft()
            if (popped_x, popped_y) == (n-1, m-1):
                return True

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                r = popped_x + dx
                c = popped_y + dy

                if r < 0 or c < 0 or r >= n or c >= m: continue
                if (r,c) in visited: continue
                if grid[r][c] not in get_compatible_streets(popped_street, grid[r][c], (dx, dy)):
                    continue

                visited.add((r,c))
                q.append((r,c,grid[r][c]))
        
        return False
