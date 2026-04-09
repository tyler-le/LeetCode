class Solution:
    def canTransform(self, start: str, result: str) -> bool:
        n, m = len(start), len(result)

        
        if n != m: return False

        arr1, arr2 = [], []

        for i, (ch1, ch2) in enumerate(zip(start, result)):
            if ch1 != "X": arr1.append((i, ch1))
            if ch2 != "X": arr2.append((i, ch2))

        if len(arr1) != len(arr2): return False


        for x, y in zip(arr1, arr2):
            print(x, y)
            x_idx, x_ch = x
            y_idx, y_ch = y

            if x_ch != y_ch: return False
            if x_idx == y_idx: continue

            if x_ch == "R" and x_idx > y_idx: return False
            if x_ch == "L" and x_idx < y_idx: return False


        return True

