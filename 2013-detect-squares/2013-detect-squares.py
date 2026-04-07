class DetectSquares:

    def __init__(self):
        self.freqs = defaultdict(int) # maps a point to its freq        

    def add(self, point: List[int]) -> None:
        row, col = point
        self.freqs[(row, col)]+=1   

    def count(self, point: List[int]) -> int:
        x, y = point
        res = 0

        for i, j in self.freqs.keys():
            diag = (i, j)
            horiz = (x, j)
            vertical = (i, y)

            if diag in self.freqs and horiz in self.freqs and vertical in self.freqs:
                # check if square or rectangle
                if not (abs(y-j) == abs(x-i)): continue

                # check distance > 0 between points
                if not abs(y-j): continue

                res+=(self.freqs[diag] * self.freqs[horiz] * self.freqs[vertical])
        
        return res

        
