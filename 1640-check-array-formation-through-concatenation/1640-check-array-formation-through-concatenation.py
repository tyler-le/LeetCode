class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        built = []
        ptr = 0

        while ptr < len(arr):
            x = arr[ptr]
            found = False
            for piece in pieces: 
                if piece[0] == x:
                    built.extend(piece)
                    ptr+=len(piece)
                    found = True
                    break
            if not found: 
                return False

        
        return built == arr

    