class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        
        """
        Intuition:
        Remove all of the X's from both strings.

        start = "RXXLRXRXL" --->    R _ _ L R _ R _ L
        result = "XRLXXRRLX" --->   _ R L _ _ R R L _

        Notice that they should have the same pattern (RLRRL == RLRRL)

        But also Rs can only move right (or stay) and Ls can only move left (or stay)
        So we must validate that each R did not move left and each L did not move right.
        """
        
        n, m = len(start), len(result)
        if n != m: return False
        
        arr1, arr2 = [], []

        for i in range(n):
            if start[i] != "X": arr1.append((i, start[i]))
            if result[i] != "X": arr2.append((i, result[i]))

        if len(arr1) != len(arr2): return False

        for (x_index, x_ch), (y_index, y_ch) in zip(arr1, arr2):
            if x_ch != y_ch: return False
            if x_ch == "R" and x_index > y_index: return False
            if x_ch == "L" and x_index < y_index: return False
        
        return True