class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        n = len(s)
        res = []

        def is_valid(start, end):
            if end - start + 1 > 3: return False
            piece_str = s[start : end + 1]
            if piece_str.startswith("0") and len(piece_str) > 1: return False
            piece = int(piece_str)
            if not 0 <= piece <= 255: return False

            return True


        def backtrack(start, path):
            nonlocal res

            if len(path) > 4: return

            if start == n:
                if len(path.copy()) == 4:
                    res.append(".".join(path.copy()))
                return 
            
            for end in range(start, n):
                if is_valid(start, end):
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res