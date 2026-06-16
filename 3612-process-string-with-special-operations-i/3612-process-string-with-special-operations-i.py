class Solution:
    def processStr(self, s: str) -> str:
        res = []
        special = set(["*", "#", "%"])

        for ch in s:
            if ch not in special: res.append(ch)
            elif ch == "*" and res: res.pop()
            elif ch == "#": res *=2
            elif ch == "%": res.reverse()

        return "".join(res)
