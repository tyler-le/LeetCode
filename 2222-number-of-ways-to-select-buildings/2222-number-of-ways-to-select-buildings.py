class Solution:
    def numberOfWays(self, s: str) -> int:
        res = 0
        hmap = defaultdict(int)

        for ch in s:
            if ch == "0":
                if "1" in hmap: hmap["10"]+=hmap["1"]
                if "01" in hmap: hmap["010"]+=hmap["01"]
                hmap["0"]+=1
            
            else:
                if "0" in hmap: hmap["01"]+=hmap["0"]
                if "10" in hmap: hmap["101"]+=hmap["10"]
                hmap["1"]+=1

        return hmap["101"] + hmap["010"]






        