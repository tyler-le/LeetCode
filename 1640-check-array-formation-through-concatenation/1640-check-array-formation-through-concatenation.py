class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        hmap = defaultdict(list)

        for piece in pieces:
            hmap[piece[0]].extend(piece)

        built = []
        ptr = 0

        while ptr < len(arr):
            x = arr[ptr]
            if not hmap[x]: return False

            built.extend(hmap[x])
            ptr+=len(hmap[x])
        
        return built == arr