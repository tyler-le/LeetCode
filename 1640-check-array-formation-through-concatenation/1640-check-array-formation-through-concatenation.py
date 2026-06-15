class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        built = []
        ptr = 0
        pieces.sort(key = lambda x : x[0])
        
        """
        Input: x - a number to search for in pieces
        Output: The piece s.t. piece[0] == x else None
        """
        def search(x):
            low, high = 0, len(pieces) - 1

            while low <= high:
                mid = low + ((high - low) // 2)
                piece = pieces[mid][0]
                if x < piece: high = mid - 1
                elif x > piece: low = mid + 1
                else: return pieces[mid]

            return None


        while ptr < len(arr):
            x = arr[ptr]
            found = False
            piece = search(x)
            if piece: 
                built.extend(piece)
                ptr+=len(piece)
            else:
                return False

        return built == arr

    